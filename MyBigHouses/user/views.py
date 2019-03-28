from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from .models import User
from house.models import House
import json
from math import floor
from hashlib import md5  # 加密密码
from django.conf import settings
from django.middleware.csrf import get_token, rotate_token
from celery_task.tasks import send_activate_email  # 发送邮件函数
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature  # 加密 激活URL
from django_redis import get_redis_connection
import datetime
from django.conf import settings
import pickle
# Create your views here.


# url: /user/login/
class LoginView(View):
    '''
    登录类视图
    url: /user/login/
    '''

    def get(self, request):
        # method == 'GET'
        get_token(request)
        return JsonResponse({})

    def post(self, request):
        # get_token(request)
        data = json.loads(request.body)
        username = data["username"]
        pwd = data["password"]
        try:
            user = User.objects.get(username=username)
        except:
            return JsonResponse({'code': 5, 'msg': u'该用户名不存在！'})
        if user:
            pwd_correct = user.password
            # 对密码hash之后与数据库中的进行对比
            if md5(pwd.encode('utf-8')).hexdigest() == pwd_correct:
                if user.is_active:
                    # 序列化user类并存储到session中
                    request.session['user'] = object_to_json(user)
                    return JsonResponse({'code': 0, 'msg': u'登录成功！','username': username})
                else:
                    # 未激活
                    return JsonResponse({'code': 3, 'msg': u'账户未激活！'})
            else:
                # 密码错误
                return JsonResponse({'code': 4, 'msg': u'密码错误！'})
        else:
            # username不存在
            return JsonResponse({'code': 5, 'msg': u'该用户名不存在！'})


# url: /user/logout
class LogoutView(View):
	# 注销 删除session中的用户名
    def get(self, request):
	    # method == 'GET'
        try:
            del request.session['user']
        except:
            return JsonResponse({'code':1, 'msg':'退出发生错误'})
        return JsonResponse({'code':0})


# 将类转化为json
def object_to_json(self):
    fields = []
    for field in self._meta.fields:
        fields.append(field.name)
    d = {}
    for attr in fields:
        if isinstance(getattr(self, attr), datetime.datetime):
            d[attr] = getattr(self, attr).strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(getattr(self, attr), datetime.date):
            d[attr] = getattr(self, attr).strftime("%Y-%m-%d")
        else:
            d[attr] = getattr(self, attr)
        return json.dumps(d)


# url: /user/active/<id>
class ActiveView(View):
    '''
    激活类视图
    url: /user/active/<id>
    '''

    def get(self, request, token):
        # 使用secret_key生成序列化器
        serializer = Serializer(settings.SECRET_KEY, 3600)
        # 使用该序列化器加载token
        try:
            info = serializer.loads(token)
        except SignatureExpired as e:
            return HttpResponse('该链接已过期')
        except BadSignature as e:
            return HttpResponse('不合法的激活链接')
        # 激活成功
        user_id = info['confirm']
        user = User.objects.get(id=user_id)
        user.is_active = 1
        user.save()
        # 激活成功，重定向到登录页面
        return HttpResponse("您已激活成功")


# url: /user/register/
class RegisterView(View):
    '''
    注册类视图
    url: /user/register/
    '''

    def get(self, request):
        get_token(request)
        return render(request, 'register.html')

    def post(self, request):
        # 接受数据
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        email = data['email']

        # 检查是否重名
        try:
            user = User.objects.get(username=username)
        except:
            user = None

        if user:
            return JsonResponse({'code': 1, "msg": "用户名已存在"})

        # 检查邮箱是否被占用
        try:
            user = User.objects.get(email=email)
        except:
            user = None
        if user:
            return JsonResponse({"code": 2, "msg": "邮箱已经被占用"})

        user = User()
        user.username = username
        user.email = email
        user.password = md5(password.encode('utf-8')).hexdigest()  # 存储密码的MD5
        user.is_active = 0  # 默认未激活
        user.save()

        # 发送验证邮件
        serializer = Serializer(settings.SECRET_KEY, 3600)  # 过期时间 3600s
        info = {'confirm': user.id}
        token = serializer.dumps(info).decode()

        # 向 celery 发送邮件任务
        send_activate_email.delay(email, username, token)

        # 重定向到登录页面
        # return redirect(reverse('login'))
        return JsonResponse({"code": 0, "msg": "注册成功! 请查看邮箱以激活账号"})


# url: /user/modify_avatar/
class UploadAvatarView(View):
    '''
    上传（修改）头像类视图
    url: /user/modify_avatar/
    '''

    def post(self, request):
        # 获取用户id
        session_user = json.loads(request.session['user'])
        user_id = session_user.get('id')

        # 获取头像文件
        avatar = request.FILES.get("file", None)
        if avatar is None:
            return JsonResponse({"code": 0, "msg": "No avatar selected"})

        try:
            user = User.objects.get(id=user_id)
        except:
            return JsonResponse({"code": 1, "msg": "无此用户"})

        # 更新数据库头像部分数据
        user.avatar = avatar
        user.save()
        return JsonResponse({"code": 0, "msg": "修改成功", "img_url": user.avatar.url})


# url: /user/info/?pag_num=xx
class GetInfoView(View):
    '''
    获取用户信息（收藏列表）类视图
    url: /user/info/?pag_num=xx
    '''


    def get(self, request):
        item_num_one_page = 5
        # 接收get请求的页码
        page_num = request.GET.get('pag_num', None)
        if page_num is None:
            page_num = 1
        else:
            try:
                page_num = int(float(page_num))
            except TypeError:
                return JsonResponse({"code": 1, "msg": "页码格式不合法！"})

        # 建立redis链接获取用户收藏信息
        conn = get_redis_connection("User&House")
        session_user = json.loads(request.session['user'])
        user_id = session_user.get('id')

        # 建立mysql链接获取用户头像信息
        try:
            user = User.objects.get(id=user_id)
        except:
            return JsonResponse({"code": 1, "msg": "无此用户"})

        user_key = "user_{}".format(user_id)
        # 用户收藏房源信息列表
        collection_infos = list()
        # 从redis中获取用户收藏房源id
        collection_list = conn.lrange(user_key, 0, -1)[::-1]
        # 获取收藏列表长度以便前端分页
        total_item_num = len(collection_list)
        # 获取收藏页数
        total_page_num = floor(total_item_num/item_num_one_page)
        # 手动分页
        collection_list = collection_list[(page_num-1)*item_num_one_page:
                                          page_num*item_num_one_page]
        # 获取分页后该页中的房源
        collection_list = [item.decode() for item in collection_list]
        for collection in collection_list:
            house_info = dict()
            house_key = "house_{}".format(collection)
            star_count = conn.hget(house_key, "star_count").decode()
            try:
                house_obj = House.objects.get(id=int(collection))
            except House.DoesNotExist:
                continue
            house_info["description"] = house_obj.description
            house_info["layout"] = house_obj.layout
            house_info["layer"] = house_obj.layer
            house_info["built_year"] = house_obj.built_year
            house_info["area"] = house_obj.area
            house_info["price"] = house_obj.price
            house_info["total_price"] = house_obj.total_price
            house_info["orientation"] = house_obj.orientation
            house_info["garden"] = house_obj.garden
            house_info["developer"] = house_obj.developer
            house_info["architecture"] = house_obj.architecture
            house_info["id"] = house_obj.id
            house_info["img_url"] = house_obj.pic_url
            house_info["star_count"] = star_count
            collection_infos.append(house_info)

        # 获取用户头像
        img_url = user.avatar.url
        return JsonResponse({"code": 0, "img_url": img_url, "data": collection_infos,
                             'page_num': page_num, 'total_page_num': total_page_num,
                             'total_item_num': total_item_num})


# url: /user/star?house_id=xxxx
class StarCountView(View):
    '''
    收藏（取消收藏）操作接口
    url: /user/star?house_id=xxxx
    '''

    def __init__(self):
        with open("./house/city_mapping_e2c.pkl", "rb") as f:
            self.city_mapping = pickle.load(f)

    def get(self, request):
        # 建立redis链接
        conn = get_redis_connection("User&House")
        try:
            # 检查是否登录
            session_user = json.loads(request.session['user'])
            user_id = session_user.get('id')
            # 检查是否 house_id 合法性
            house_id = request.GET.get('house_id', None)
            if house_id is None:
                return JsonResponse({"code": 1, "msg": "未提供房源 id "})
            try:
                house_id = int(house_id)
            except TypeError:
                return JsonResponse({"code": 2, "msg": "房源 id 不合法"})

            # 检查是否已收藏
            user_key = "user_{}".format(user_id)
            star_list = conn.lrange(user_key, 0, -1)
            star_list = [item.decode() for item in star_list]

            if str(house_id) in star_list:
                star_flag = True
            else:
                star_flag = False

        except KeyError:
            return JsonResponse({"code": 3, "msg": "请先登录"})

        house_key = "house_{}".format(house_id)
        # 有这个收藏，说明要做取消收藏的动作
        if star_flag:
            conn.lrem(user_key, 0, house_id)
            conn.hincrby(house_key, "star_count", -1)
            star_flag = False

        # 没有这个收藏，说明要做加入收藏的动作
        else:
            conn.lpush(user_key, house_id)
            conn.hincrby(house_key, "star_count", 1)
            star_flag = True

        # 获取更新之后的收藏量
        star_count = conn.hget(house_key, "star_count").decode()

        # 更新该房子所在城市收藏量的 top_N
        house_record = House.objects.get(id=house_id)
        city = house_record.city
        for k, v in self.city_mapping.items():
            if v == city:
                city_en = k

        top_key = "{}_topN".format(city_en)
        # 将 <star_count, house_id> 添加到 zset 中
        k_v = dict()
        k_v[house_id] = star_count
        conn.zadd(top_key, k_v)

        return JsonResponse({"code": 0, "star_count": star_count, "star_flag": star_flag})



