<template>
  <div v-bind:class="{body: true}">
	  <div v-bind:class="{background: true}">
    	<div v-bind:class="{register_window: true}">

    			<img src="../assets/user.png" style="height: 30px; width: 30px;" />
      		<div style="margin-top: 10px; max-height: 260px;min-height: 260px;max-width: 250px;min-width: 250px;padding-left: 10px;">
      			  <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
			          <el-form-item prop="email">
				          <el-input v-bind:class="{text_input: true}" v-model="ruleForm.email" placeholder="email"></el-input>
			          </el-form-item>
			          <el-form-item prop="username">
				          <el-input v-model="ruleForm.username" v-bind:class="{text_input: true}" placeholder="username"></el-input>
			          </el-form-item>
			          <el-form-item prop="password">
				          <el-input v-model="ruleForm.password" autocomplete="off" type="password" v-bind:class="{text_input: true}" placeholder="password"></el-input>
			          </el-form-item>
			          <el-form-item prop="confirm_password">
				          <el-input v-model="ruleForm.confirm_password" autocomplete="off" type="password" placeholder="confirm password" v-bind:class="{text_input: true}"></el-input>
			          </el-form-item>
			            <el-button type="primary" @click="submitForm('ruleForm')" v-bind:class="{button: true, register_btn:true}" :loading="register_loading_flag">注册</el-button></br>
			          <el-form-item style="width: 200px; margin-left:70px; text-align: right; margin-top:3px">
			            <el-button @click="resetForm('ruleForm')" v-bind:class="{button: true, reset_btn: true}">重置</el-button>
			          </el-form-item>
			        </el-form>
	        </div>
      </div>
		</div>
  </div>
</template>

<script>
	import store from '@/store'
	import global_ from '@/components/Global'
	import iView from 'iview';
	export default {
		data() {
			//第一次输入密码验证
			var validatePass = (rule, value, callback) => {
				if (value === '') {
					callback(new Error('请输入密码'));
				} else {
					if (this.ruleForm.confirm_password !== '') {
						this.$refs.ruleForm.validateField('confirm_password');
					}
					callback();
				}
			};
			//第二次输入密码验证
			var validatePass2 = (rule, value, callback) => {
				if (value === '') {
					callback(new Error('请再次输入密码'));
				} else if (value !== this.ruleForm.password) {
					callback(new Error('两次输入密码不一致!'));
				} else {
					callback();
				}
			};

			return {
				
				register_loading_flag: false,//提交注册加载
				ruleForm: {
					//邮箱，用户名，密码，确认密码双向绑定
					email: '',
					username: '',
					password: '',
					confirm_password: ''
				},
				rules: {
					//邮箱验证
					email: [{
							required: true,//必须输入
							message: '请输入邮箱地址',
							trigger: 'blur'
						},
						{
							type: 'email',//邮箱类型
							message: '请输入正确的邮箱地址',
							trigger: ['blur', 'change']
						}
					],
					//用户名验证
					username: [{
							
							required: true,//必须输入
							message: '请输入用户名',
							trigger: 'blur'
						},
						{
							min: 1,//最小长度1
							max: 20,//最大长度20
							message: '长度在 1 到 20 个字符',
							trigger: 'blur'
						}
					],
					//密码验证
					password: [{
						validator: validatePass,
						trigger: 'blur'
					}, {
							required: true,
							message: '请输入密码',
							trigger: 'blur'
						},
						{
							min: 6,
							max: 30,
							message: '长度在 6 到 30 个字符',
							trigger: 'blur'
						}
					],
					confirm_password: [{
						validator: validatePass2,
						trigger: 'blur'
					}, ],
				}
			};
		},
		methods: {
			submitForm(formName) {
				this.register_loading_flag = true,
				this.$refs[formName].validate((valid) => {
					if (valid) {
						//获取csrftoken
						var arr = this.getCookie('csrftoken')
						//通过post请求提交表单
						this.$ajax({
							method: 'post',
							url: global_.IpUrl + '/user/register/',
							data: {
								username: this.ruleForm.username,
								password: this.ruleForm.password,
								email: this.ruleForm.email
							},
							headers: {

								'Content-Type': 'application/x-www-form-urlencoded',

								'X-CSRFToken': arr
							}
						}).then(function(response) {
							this.register_loading_flag = false
							if (response.data.code === 0) {
								//成功，提示激活邮箱
								iView.Message.info('注册成功,请至邮箱激活您的账号')
							} else {
								iView.Message.info(response.data.msg)
							}
						}.bind(this))
					} else {
						this.register_loading_flag = false
						return false;
					}
				});
				
			},
			resetForm(formName) {
				this.$refs[formName].resetFields();
			},
			getCookie(name) { //获取cookie函数
				name = name + "=";
				var start = document.cookie.indexOf(name),
					value = null;
				if (start > -1) {
					var end = document.cookie.indexOf(";", start);
					if (end == -1) {
						end = document.cookie.length;
					}
					value = document.cookie.substring(start + name.length, end);
				}
				return value;
			}
		}
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
	  height:800px;
	  background-image:url(../assets/login_back.jpg);
	  background-repeat: no-repeat;
	  background-size:100% 100%;
	  padding-top: 160px;
	  text-align: center;
	}

  .register_window{
    border-radius:20px;
    width: 300px;
    height: 400px;
    opacity:0.5;
    background-color: white;
    text-align:center;
    margin:0 auto;
    padding-top: 20px;
  }

  .button{
	  opacity: 100%;
	  border-radius:10px;
	  display: inline-block;
	  -webkit-border-radius: 30px;
	  -moz-border-radius: 30px;
	  width: 80px;
	  box-shadow: 0;
	  border-style: solid;
	  padding: 4px;
	  background: transparent;
	  border-color: #009688;
	  color: black;
	  margin-left: 0px;
	  margin-top: 0px;
  }

  .button:hover{
	  cursor: pointer;
  }

  .register_btn{
    margin-left: 38px;
    width:200px;
    height: 40px;
  }

  .reset_btn{
    border-width: 0;
  }

  .text_input{
	  width: 200px;
	  margin: 0px;
	  padding: 0px;
	  opacity: 100%;
	  display: inline-block;
	  border-color: darkgray;
	  text-align: center;
	  background-color: white;
	  color: black;
	  margin-left: -60px;
  }

  .el-input__inner::-webkit-input-placeholder{   /* WebKit browsers */
    color: black;
  }
  .el-input__inner::-moz-placeholder{   /* Mozilla Firefox 19+ */
    color: black;
  }
  .el-input__inner:-moz-placeholder{    /* Mozilla Firefox 4 to 18 */
    color: black;
  }
  .el-input__inner:-ms-input-placeholder{  /* Internet Explorer 10-11 */
    color: black;
  }

</style>

