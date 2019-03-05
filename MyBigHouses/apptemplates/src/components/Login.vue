<template>

	<div style="margin-top:60px; width: 450px; margin:60px auto">
		<el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
			<el-form-item label="用户名" prop="username">
				<el-input v-model="ruleForm.username"></el-input>
			</el-form-item>
			<el-form-item label="密码" prop="userpassword">
				<el-input v-model="ruleForm.userpassword"></el-input>
			</el-form-item>

			<el-form-item>
				<el-checkbox v-model="checked" style="color:#a0a0a0;float:left">一周内自动登录</el-checkbox>
			</el-form-item>

			<el-form-item>
				<el-button type="primary" @click="submitForm('ruleForm')">立即登陆</el-button>
				<el-button @click="register_route()">注册账号</el-button>
			</el-form-item>
		</el-form>
	</div>

</template>

<script>
	import store from '@/store'
	export default {
		name: 'HelloWorld',
		store,
		data() {
			return {
				ruleForm: {
					username: '',
					password: '',
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
				url: 'http://127.0.0.1:8000/user/login/',
			})
		},
		methods: {
			submitForm(formName) {
				this.$refs[formName].validate((valid) => {
					if (valid) {
						var arr = this.getCookie('csrftoken')
						this.$ajax({
							method: 'post',
							url: 'http://127.0.0.1:8000/user/login/',
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
								alert("登陆成功")
								sessionStorage.setItem('username', response.data.username)
								var usr = sessionStorage.getItem("username")
								store.commit('change_isLogin', usr)
								loaclstorage.setItem("Flag", "isLogin")
								setTimeout(this.go, 1000);
							} else {
								alert(response.data.msg)
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
		},
	}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
