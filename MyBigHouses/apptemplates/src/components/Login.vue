<template>
  <div v-bind:class="{body: true}">
	  <div v-bind:class="{background: true}">
    	<div v-bind:class="{login_window: true}">
    			<img src="../assets/user.png" style="height: 40px; width: 40px;margin-top: 19px;" />
      		<div style="margin-top: 20px; max-height: 245px;min-height: 245px;max-width: 250px;min-width: 250px;padding-left: 10px;">
      			  <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="20px" class="demo-ruleForm">
			          <el-form-item prop="username" >
				          <el-input v-model="ruleForm.username" v-bind:class="{text_input: true}" placeholder="请输入用户名"></el-input>
			          </el-form-item>

			           <el-form-item prop="userpassword">

				           <el-input v-model="ruleForm.userpassword" v-bind:class="{text_input: true}" type="password" placeholder="请输入密码"></el-input>

			           </el-form-item>

			          <el-form-item style="width: 100px; text-align: left; margin-left: 10px;margin-top: -10px;">
				          <el-checkbox v-model="checked" style="color:black;float:left">一周内自动登录</el-checkbox>
			          </el-form-item>

			          <el-form-item style="margin-left: 5px;">
				          <el-button type="primary" @click="submitForm('ruleForm')" v-bind:class="{button: true}">立即登陆</el-button>
				        </el-form-item>

				      <el-form-item style="width: 100px; text-align: right;margin-left: 150px;">
				          <el-button @click="register_route()" v-bind:class="{register_btn: true}">注册账号</el-button>
			          </el-form-item>
		          </el-form>
      		</div>
		</div>
      </div>
  </div>
</template>


<script>
	import store from '@/store'
	import iView from 'iview';
	import global_ from '@/components/Global'
	import {
		getCookie,
		setCookie,
		delCookie
	} from '@/utils/utils'
	export default {
		name: 'HelloWorld',
		store,
		data() {
			return {
				ruleForm: {
					username: '',
					password: '',
					checked: false
				},
				rules: {
					username: [{
							required: true,
							message: '请输入用户名',
							trigger: 'blur'
						},
						{
							min: 1,
							max: 20,
							message: '长度在 1 到 20 个字符',
							trigger: 'blur'
						}
					],
					userpassword: [{
							required: true,
							message: '请输入密码',
							trigger: 'blur'
						},
						{
							min: 6,
							max: 15,
							message: '长度在 6 到 15 个字符',
							trigger: 'blur'
						}

					],
				},
				checked: false,
			};
		},
		mounted() {
			this.$ajax({
				method: 'get',
				url: global_.IpUrl+'/user/login/',
			})
		},
		methods: {
			submitForm(formName) {
				this.$refs[formName].validate((valid) => {
					if (valid) {
						console.log(global_.IpUrl)
						var arr = getCookie('csrftoken')
						this.$ajax({
							method: 'post',
							url: global_.IpUrl+'/user/login/',
							data: {
								username: this.ruleForm.username,
								password: this.ruleForm.userpassword,
								ischecked: this.checked
							},
							headers: {
								'Content-Type': 'application/x-www-form-urlencoded',
								'X-CSRFToken': arr
							}
						}).then(function(response) {
							if (response.data.code === 0) {
								iView.Message.info('登录成功')
								store.commit('change_isLogin', response.data.username)
								if(this.ruleForm.checked){
									setCookie("username", response.data.username, 7*24*60*60*1000)
									setCookie("Flag", "isLogin", 7*24*60*60*1000)
								}else{
									setCookie("username", response.data.username)
									setCookie("Flag", "isLogin")
								}
								//window.localStorage.setItem("username", response.data.username)
								//window.localStorage.setItem("Flag", "isLogin")
								setTimeout(this.go, 1000);
							} else {
								iView.Message.info(response.data.msg)
							}
						}.bind(this))
					} else {
						console.log('error submit!!');
						return false;
					}
				});
			},
			go() {
				this.$router.go(-1)
			},

			register_route() {
				this.$router.push({
					path: "/register"
				})
			},
		},
	}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .body{
      width: 100%;
	  height: 100%;
	  padding:0px;
      overflow: hidden;
	  display:block;
	  position:relative;
      }
	.background {
	  width:100%;
	  height:700px;
	  background-image:url(../assets/login_back.jpg);
	  background-repeat: no-repeat;
	  background-size:100% 100%;
	  padding-top: 160px;
	 }
    .login_window{
      border-radius:20px;
      width: 300px;
      height: 360px;
      opacity:0.5;
      background-color: white;
      text-align:center;
      margin:0 auto;
      padding-top: 1px;
    }
.button{
	opacity: 100%;
	border-radius:10px;
	display: inline-block;
	-webkit-border-radius: 30px;
	-moz-border-radius: 30px;
	width: 200px;
	box-shadow: 0;
	border-style: solid;
	background: transparent;
	border-color: #009688;
	color: black;
	margin-top: -20px;
}

    .button:hover{
	    cursor: pointer;
    }
.text_input{
	width: 200;
	margin: 0px;
	opacity: 100%;
	display: inline-block;
	text-align: center;
	padding-left: 5px;
}
.register_btn{
	border-width:0px;
	outline: 0 !important;
	background:transparent;
	color: black;
	margin-bottom: 2px;
}

.register_btn:hover{
	cursor: pointer;
}
input::-webkit-input-placeholder{  
        color:black;
}
</style>
