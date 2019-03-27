<template>
	<div style="width: 100%;height: 100%;padding-left: 0px;" v-loading.fullscreen.lock="fullscreenLoading">
		<div style="background-color: lightgray;width: 100%;max-height: 200px;padding-top:100px;padding-left: 0px;">
			<div style="width: 300px;height: 100px;margin-left: 150px;text-align: left;padding: 0px;">
				<!-- <div style="background: #AAAAAA;max-height: 120px;max-width: 120px;border-radius:8px;float: left;"> -->
				<el-upload class="avatar-uploader" name="file" :action="post_img_url" :headers="import_headers" :show-file-list="false"
				 :on-success="handleAvatarSuccess" :before-upload="beforeAvatarUpload">
					<img v-if="imageUrl" :src="imageUrl" class="avatar">
					<i v-else class="el-icon-plus avatar-uploader-icon"></i>
				</el-upload>
				<!-- <img src="../assets/user.png" style="max-height: 120px;max-width: 120px;"/> -->
				<!-- </div> -->
				<p style="font-size: 15px;font-weight: 300;max-height: 20px;margin-top: 0;margin-left: 150px;">{{user_name}}</p>
				<!-- <p style="font-size: 15px;font-weight: 300;max-height: 20px;margin-top:0;margin-left: 150px;">12345678@qq.com</p> -->
				<!-- <el-button size="small" round style="margin-top: 3px;margin-left: 20px;">编辑个人资料</el-button> -->
			</div>
		</div>
		<div class="body">
			<div class="list_content">
				<div style="margin-top: 50px;min-height: 30px;min-width: 80%;">
					<p style="font-size: 25px;float: left;"><b>我的收藏</b></p>
				</div>
				<div class="line"></div>

				<ul class="list">
					<li class="collect" v-for="(o, index) in favor_info" key='o.id'>
						<img :src="o.img_url" class="item_img" />

						<div class="block">
							<p style="font-size: 18px;font-weight: 500;cursor: pointer;" @click="go_to_detail(o.id,index)">
								{{o.description}}
							</p>
							<p class="desCollect">
								{{o.layout}}，{{o.area}}平米，{{o.layer}}
								{{o.garden}}，{{o.architecture}}，{{o.built_year}}
								{{o.developer}}
							</p>
							<div class="cancelCollect">
								<p style="font-size: 12px;font-weight: 300;margin-left: 10px; cursor: pointer;" @click="cancel_favour(o.id)">
									取消收藏
								</p>
							</div>

						</div>
						<div class="item_right">
							<p class="textColor">
								{{o.total_price}}万
							</p>
							<p style="font-size: 12px;font-weight: 300;">
								单价：{{o.price}}元
							</p>
							<p style="font-size: 12px;font-weight: 300;margin-top: 20px;">
								{{o.star_count}}人已收藏
							</p>
						</div>
						<div class="line1"></div>
					</li>
				</ul>

				<v-pagination :total="total" :current-page='current' @pagechange="pagechange"></v-pagination>


			</div>

		</div>

	</div>
</template>

<script>
	import store from '@/store'
	import global_ from '@/components/Global'
	import pagination from '@/components/MyPagenation'
	import {
		getCookie,
		setCookie,
		delCookie
	} from '@/utils/utils'
	export default {
		//引入分页组件
		components: {
			'v-pagination': pagination,
		},
		data() {
			return {
				//请求地址ip
				post_img_url: global_.IpUrl + '/user/modify_avatar',
				imageUrl: '',//头像url
				user_name: store.state.UserInfo.username,//用户名
				import_headers: {
					// 'Content-Type': 'multipart/form-data',
					'X-CSRFToken': getCookie('csrftoken')
				},
				favor_info: [],//信息了列表
				//分页实现内容
				total: 0, // 记录总条数
				display: 5, // 每页显示条数
				current: 1, // 当前的页数
			};

		},
		created() {
			//获取用户头像
			this.getAvatar()
		},
		mounted() {
			//获取收藏信息
			this.getList()
		},
		methods: {
			
			getList() {
				//加载等待
				const loading = this.$loading({
					lock: true,
					text: 'Loading',
					spinner: 'el-icon-loading',
					background: 'rgba(255,255,255,0.8)'
				});
				//将收藏信息置空
				this.favor_info = []
				let url = global_.IpUrl + '/user/get_info/?pag_num=' + this.current
				this.$ajax({
					url: url,
					method: 'get',
				}).then(function(response) {
					if (response.data.code === 0) {
						var favor = response.data.data
						for (var i = 0; i < favor.length; i++) {
							var temp = {}
							//展示收藏信息
							temp["description"] = favor[i].description
							temp["layout"] = favor[i].layout
							temp["layer"] = favor[i].layer
							temp["built_year"] = favor[i].built_year
							temp["area"] = favor[i].area
							temp["price"] = favor[i].price
							temp["total_price"] = favor[i].total_price
							temp["orientation"] = favor[i].orientation
							temp["garden"] = favor[i].garden
							temp["developer"] = favor[i].developer
							temp["architecture"] = favor[i].architecture
							temp["id"] = favor[i].id
							temp["img_url"] = favor[i].img_url
							temp["star_count"] = favor[i].star_count
							this.favor_info.push(temp)
							this.total = response.data.total_item_num
							
						}
						loading.close();
					} else {
						iView.Message.info(response.data.msg)
					}
				}.bind(this))

			},
			//页码改变触发事件
			pagechange(page) {
				this.current = page
				this.getList()
			},
			//获取用户头像url
			getAvatar() {
				this.$ajax({
					method: 'get',
					async: false,
					url: global_.IpUrl + '/user/get_info',
				}).then(function(response) {
					if (response.data.code == 0) {
						this.imageUrl = global_.IpUrl + '/' + response.data.img_url
					} else {
						iView.Message.info(response.data.msg)
					}
				}.bind(this))
			},
			//上传头像
			handleAvatarSuccess(response, file) {
				if (response.code == 0) {
					// this.imageUrl = URL.createObjectURL(file.raw);
					this.imageUrl = global_.IpUrl + '/' + response.img_url
				} else {
					iView.Message.info(response.msg)
				}
			},
			//检查上传头像是否合法
			beforeAvatarUpload(file) {
				const isJPG = file.type === 'image/jpeg';
				const isLt2M = file.size / 1024 / 1024 < 2;

				if (!isJPG) {
					this.$message.error('上传头像图片只能是 JPG 格式!');
				}
				if (!isLt2M) {
					this.$message.error('上传头像图片大小不能超过 2MB!');
				}
				return isJPG && isLt2M;
			},
			//取消收藏
			cancel_favour(id, index) {
				var _this = this
				_this.$ajax({
					method: 'get',
					url: global_.IpUrl + "/user/star?house_id=" + id
				}).then(function(response) {
					if (response.data.code === 0) {
						_this.$router.go(0)
					} else {
						if (response.data.code === 2) {
							iView.Message.info("请先登录")
							setTimeout(this.go, 1000);
						}
					}
				})
			},
			//进入收藏房源详情页
			go_to_detail(id) {
				this.$router.push({
					path: 'ItemPage',
					query: {
						HouseId: id
					}
				})
			}

		}
	}
</script>

<style scoped>
	.pageNumber {
		width: 950px;
		position: relative;
		margin-top: 30px;
	}

	.line {
		height: 3px;
		width: 30%;
		background: black;
		overflow: hidden;
		margin-top: 40px;
	}

	.line1 {
		height: 1px;
		width: 90%;
		background: lightgrey;
		overflow: hidden;
		margin-top: 10px
	}

	.body {
		width: 100%;
		height: 1000px;
		padding-left: 50%;
		margin-top: 40px;
	}

	.item {
		display: inline-block;
		vertical-align: middle;
		min-width: 32px;
		height: 32px;
		line-height: 30px;
		margin-right: 4px;
		text-align: center;
		list-style: none;
		background-color: #fff;
		user-select: none;
		cursor: pointer;
		font-family: Arial;
		font-weight: 500;
		border: 1px solid #dcdee2;
		border-radius: 4px;
		transition: border .2s ease-in-out, color .2s ease-in-out;
	}

	.item a {
		font-family: Monospaced Number;
		margin: 0 6px;
		text-decoration: none;
		color: #515a6e;
	}

	.collect {
		min-height: 150px;
		width: 950px;
		max-height: 150px;
		float: left;
		text-align: left;
		padding-top: 0;
		position: relative;
		margin-top: 20px;
		list-style: none;
	}

	.textColor {
		font-size: 28px;
		font-weight: 400;
		margin-top: 10px;
		color: rgb(252, 124, 0);
	}

	.avatar-uploader .el-upload {
		border: 1px dashed #d9d9d9;
		border-radius: 6px;
		cursor: pointer;
		position: relative;
		overflow: hidden;
	}

	.avatar-uploader .el-upload:hover {
		border-color: #409EFF;
	}

	.avatar-uploader-icon {
		font-size: 28px;
		color: #8c939d;
		width: 178px;
		height: 178px;
		line-height: 178px;
		text-align: center;
	}

	.avatar {
		width: 178px;
		height: 178px;
		display: block;
	}

	.list_content {
		width: 950px;
		height: 950px;
		margin-left: -475px;
		padding-top: 30px;
	}

	.list {
		width: 100%;
		position: relative;
		overflow: hidden;
	}

	.item_img {
		max-height: 145px;
		max-width: 200px;
		min-height: 145px;
		min-width: 200px;
		background-size: 100% 100%;
		display: inline-block;
	}

	.desCollect {
		font-size: 12px;
		font-weight: 300;
		margin-left: 10px;
		height: 80px;
		width: 400px;
	}

	.cancelCollect {
		width: 100px;
		margin-top: 20px;
		height: 20px;
	}

	.block {
		width: 500px;
		height: 150px;
		display: inline-block;
		padding: 0;
		position: absolute;
		top: 0px;
		left: 210px;
	}

	.item_right {
		height: 150px;
		width: 150px;
		display: inline-block;
		padding: 0;
		position: absolute;
		top: 0px;
		left: 800px;
	}
</style>
