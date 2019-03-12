<template>
	<div style="width: 100%;height: 50px;background-color: white;color: black;min-width: 1273px;">
		<el-menu router :default-active="$route.path" class="el-menu-demo" mode="horizontal" @select="handleSelect">
			<img src="../assets/logo1.png" style="max-height: 40px;float: left;margin-left: 80px;margin-top: 5px;" />
			<p style="float:left;font-size: 20px;color: black;font-weight: 700;margin-left: 10px;margin-top: 15px;">
				My Big Houses
			</p>

			<i class="el-icon-location" style="max-height: 20px;float: left;margin-left: 100px;margin-top: 25px;"></i>
			<p style="float:left;font-size: 12px;color: black;font-weight: 300;margin-left: 10px;margin-top: 25px;"@click="select_area()">
				{{getCity}}
			</p>

			<el-menu-item style="margin-left: 20%;color: black;font-size: 18px;" index="/">主页</el-menu-item>
			<el-menu-item index="/price_condition" style="color: black;font-size: 18px;">房价</el-menu-item>
			<el-menu-item style="color: black;font-size: 18px;" index="" @click="show()">预测</el-menu-item>
			<el-menu-item style="color: black;font-size: 18px;" index="/SelectHouse">挑房</el-menu-item>

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
		mounted() {

		},

		computed: {
			isLogin() {
				return store.state.isLogin
			},

			getusername() {
				return store.state.UserInfo.username
			},
			getCity(){
				return store.state.area.city
			}
		},
		methods: {
			show() {
				alert(this.isLogin)
			},
			loginout() {
				store.commit('change_LoginOut')
				delCookie("username")
				delCookie("Flag")
				iView.Message.info('退出成功')
			},
			select_area(){
				this.$router.push({path: '/AreaSelect'})
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
