<template>
	<div style="width: 100%;height: 50px;background-color: white;color: black;min-width: 1050px;">
		<el-menu router :default-active="$route.path" class="el-menu-demo" mode="horizontal" @select="handleSelect">
			<div style=" cursor: pointer;" @click="go_to_main_page()">
			<img src="../assets/logo1.png" style="max-height: 40px;float: left;margin-left: 80px;margin-top: 5px;outline:none;"/>
			<p style="float:left;font-size: 20px;color: black;font-weight: 700;margin-left: 10px;margin-top: 15px;outline:none;">
				My Big Houses
			</p>
			</div>
			<i class="el-icon-location" style="max-height: 20px;float: left;margin-left: 50px;margin-top: 25px;"></i>
			<p style="float:left;font-size: 12px;color: black;font-weight: 300;margin-left: 10px;margin-top: 25px;cursor: pointer;" @click="select_area()">
				{{getCity}}
			</p>

			<el-menu-item style="margin-left: 15%;color: black;font-size: 18px;" index="/">主页</el-menu-item>
			<el-menu-item index="/price_condition" style="color: black;font-size: 18px;">房价</el-menu-item>
			<el-menu-item style="color: black;font-size: 18px;" index="/PricePredict">预测</el-menu-item>
			<el-menu-item style="color: black;font-size: 18px;" index="/HouseChoosing">挑房</el-menu-item>

			<el-menu-item style="float: right;color: black;" index="/register" v-if="!isLogin">注册</el-menu-item>
			<el-menu-item index="/login" style="float: right;color: black;" v-if="!isLogin">
				<img src="../assets/user.png" style="max-height: 12px;float: left;margin-top: 24px;margin-right: 5px;" />
				登录
			</el-menu-item>

			<el-submenu style="float: right;color: black;margin-right: 5%;" v-else>
				<template slot="title">{{getusername}}</template>
				<el-menu-item index='/UserInfo'>查看个人信息</el-menu-item>
				<el-menu-item index='' @click="loginout()">退出登录</el-menu-item>
			</el-submenu>

		</el-menu>
	</div>

</template>

<script>
	import store from '@/store'
	import iView from 'iview'
	import BMap from 'BMap';
	import global_ from '@/components/Global'
	import { MessageBox } from 'element-ui';
	import {
		getCookie,
		setCookie,
		delCookie
	} from '@/utils/utils'
	export default {
		store,
		data() {
			return {

			};
		},
		// create钩子，挂载前调用
		created() {
			//localstorage中的省份信息，如过为空，说明第一次登陆
			var local_province = localStorage.getItem("province")
			var self = this
			//省份为空，获取当前定位
			if (local_province == null) {
				//调用百度定位接口
				const geolocation = new BMap.Geolocation();
				let self = this
				let city
				let province
				geolocation.getCurrentPosition(function getinfo(position) {
					city = position.address.city; //获取城市信息
					province = position.address.province; //获取省份信息
					
					MessageBox.confirm('是否切换到'+city+'?', '提示', {
						confirmButtonText: '确定',
						cancelButtonText: '取消',
						type: 'info'
					}).then(() => {
						//点击确认
						var arr = city.split('')
						//去除“市”字
						if(arr[arr.length-1]=="市"){
							arr.splice(arr.length-1,1)
							var new_city = arr.join('')
						}
						
						arr = province.split('')
						//去除“省”字
						if(arr[arr.length-1]=="省"){
							arr.splice(arr.length-1,1)
							var new_province = arr.join('')
						}
						var area = {}
						area["province"] = province
						area["city"] = new_city
						area["area"] = ''
						area["street"] = ''
						area["province_eng"] = global_.city_mapping[new_province]
						area["city_eng"] = global_.city_mapping[new_city]
						area["area_eng"] = ''
						area["street_eng"] = ''
						//修改全局参数
						store.commit('change_AreaInfo', area)
						//刷新页面
						self.$router.go(0)
					}).catch(() => {
						//点击取消
					});

					// 		store.state.area.city = city
					// 		store.state.area.province = province
					// sessionStorage.setItem('currentCity', city.substr(0, city.length - 1))
				}, function(e) {}, {
					provider: 'baidu'
				});
			}
		},
		mounted() {

		},

		computed: {
			// 获取是否登陆信息
			isLogin() {
				return store.state.isLogin
			},
			//获取用户名
			getusername() {
				return store.state.UserInfo.username
			},
			//获取城市信息
			getCity() {
				return store.state.area.city
			}
		},
		methods: {
			go_to_main_page(){
				this.$router.push({
					path: '/'
				})
			},
// 			show() {
// 				alert(this.isLogin)
// 			},
// 			get_ip_city() {
// 				this.$ajax({
// 					methods: 'get',
// 					dataType: 'JSONP',
// 					url: "http://api.map.baidu.com/location/ip?ak=zDGd0AGNoHiQRg40IEED6bIGlQEgXd8K&coor=bd09ll&callback=showLocation",
// 					jsonp: 'callback',
// 					jsonpCallback: "callback",
// 
// 				}).then(function(response) {
// 					if (response.data.status == 0) {
// 						var area = {}
// 						area["province"] = response.data.content.address_detail.province
// 						area["city"] = response.data.content.address_detail.city
// 						area["area"] = ''
// 						area["street"] = ''
// 						area["province_eng"] = "jiangsu"
// 						area["city_eng"] = "suzhou"
// 						area["area_eng"] = ''
// 						area["street_eng"] = ''
// 						store.commit('change_AreaInfo', area)
// 					} else {
// 						iView.message.info("error code:" + response.data.status)
// 					}
// 				}.bind(this))
// 			},
			//注销按键
			loginout() {
				store.commit('change_LoginOut')
				delCookie("username")
				delCookie("Flag")
				iView.Message.info('退出成功')
				//返回到登陆页面
				this.$router.push({
					name:'MainPage',
					})
			},
			//跳转到选择区域界面
			select_area() {
				this.$router.push({
					path: '/AreaSelect'
				})
			}


		}
	}
</script>

<style scoped>
	.item {
		background-color: red;
		font-size: 20px;
		color: black;
		margin-left: 10px;
	}
</style>
