<template>
	<div style="width: 100%;height: 50px;background-color: white;color: black;">
		<el-menu router :default-active="$route.path" class="el-menu-demo" mode="horizontal" @select="handleSelect">
			<img src="../assets/logo1.png" style="max-height: 40px;float: left;margin-left: 80px;margin-top: 5px;"/>
			<p style="float:left;font-size: 20px;color: black;font-weight: 700;margin-left: 10px;margin-top: 15px;">
				My Big Houses
			</p>
			
			<i class="el-icon-location" style="max-height: 20px;float: left;margin-left: 100px;margin-top: 25px;"></i>
			<p style="float:left;font-size: 12px;color: black;font-weight: 300;margin-left: 10px;margin-top: 25px;">
				苏州
			</p>
			
			<el-menu-item style="margin-left: 20%;color: black;font-size: 18px;" index="/">主页</el-menu-item>
			<el-menu-item index="/price_condition" style="color: black;font-size: 18px;">房价</el-menu-item>
			<el-menu-item style="color: black;font-size: 18px;" index="" @click="show()">预测</el-menu-item>
			<el-menu-item style="color: black;font-size: 18px;" index="/user">挑房{{isLogin}}</el-menu-item>
			<el-menu-item style="float: right;color: black;" index="/register" >注册</el-menu-item>
			<el-menu-item index="/user/login" style="float: right;color: black;">
			<img src="../assets/user.png" style="max-height: 12px;float: left;margin-top: 24px;margin-right: 5px;"/>
				登录
			</el-menu-item>
			<el-menu-item v-else>注销</el-menu-item>
			
		</el-menu>		
	</div>
		
		<!--	
		<el-menu router :default-active="$route.path" class="el-menu-demo" mode="horizontal" @select="handleSelect" background-color="white" text-color="#fff" active-text-color="#red">

	
		<el-menu-item index="/user/login" >登陆</el-menu-item>
		<el-menu-item v-else>注销</el-menu-item>
		    </el-menu>-->
</template>

<script>
	import store from '@/store'
export default {
		store,
        data() {
            return {
                activeIndex: '1',
                activeIndex2: '1',

            };
        },
		mounted(){
			var username = sessionStorage.getItem('username')
				
			if(username!=''){
				console.log(store.state.isLogin)
			}
			
			},
			
		computed:{
			isLogin(){
				return store.state.isLogin
			}
		},
        methods: {
			show(){
				alert(this.isLogin)
			}
        }
    }
</script>

<style scoped>
.item{
	background-color: red;
	font-size: 20px;
	color: black;
	margin-left: 10px;
}
</style>
