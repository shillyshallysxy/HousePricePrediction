<template>
    <div style="margin-top:60px;">
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
    <el-form-item label="邮箱" prop="email">
        <el-input v-model="ruleForm.email"></el-input>
    </el-form-item>
    <el-form-item label="用户名" prop="username">
        <el-input v-model="ruleForm.username"></el-input>
    </el-form-item>
    <el-form-item label="密码" prop="password">
        <el-input type="password" v-model="ruleForm.password" autocomplete="off"></el-input>
    </el-form-item>
    <el-form-item label="确认密码" prop="confirm_password">
        <el-input type="password" v-model="ruleForm.confirm_password" autocomplete="off"></el-input>
    </el-form-item>
  

  
    <el-button type="primary" @click="submitForm('ruleForm')">注册</el-button>
    <el-button @click="resetForm('ruleForm')">重置</el-button>
    </el-form-item>
    </div>
</el-form>
</template>

<script>
export default {
    data() {
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
        ruleForm: {
          email: '',
          username: '',
          password: '',
          confirm_password: ''
        },
        rules: {
          email: [
            { required: true, message: '请输入邮箱地址', trigger: 'blur' },
            { type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur', 'change'] }
          ],  
          username: [
            { required: true, message: '请输入用户名', trigger: 'blur' },
            { min: 1, max: 20, message: '长度在 1 到 20 个字符', trigger: 'blur' }
          ],
          password: [
            { validator: validatePass, trigger: 'blur' }, 
          ],
          confirm_password: [
            { validator: validatePass2, trigger: 'blur' }, 
          ],
        }
      };
    },
    methods: {
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            alert(this.ruleForm);
            var arr = this.getCookie('CSRFtoken')
            alert(arr)
            
            this.$ajax({
              method: 'post',
              url:'http://localhost:8000/user/register/',
              data :{
                username: this.ruleForm.username,
                password: this.ruleForm.userpassword,
                email: this.ruleForm.email
              },
              headers:{
              'Accept': '*/*',
              'Content-Type': 'application/x-www-form-urlencoded',
              'Access-Control-Allow-Origin': '*',
              'Access-Control-Allow-Methods': 'DELETE, POST, GET, OPTIONS',
              'Access-Control-Allow-Headers': 'Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With',
              'X-CSRFtoken': arr
              }
          }).then(function(response){
            alert(response.data.msg)
            if(response.data.code === 0){
              window.location = ''  //登录成功后跳转到home页面
              setCookie('login', 'success', 15)
              setCookie('username', response.data.data.username, 15)
              setCookie('userid', response.data.data.id, 15)
            } else {
              vm.$message.error('Login failed!!');
            }
          })
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      },
      getCookie(name) {
        var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
        if (arr = document.cookie.match(reg))
          return (arr[2]);
        else
          return null;
        }
    }
  }
</script>

<style>
</style>
