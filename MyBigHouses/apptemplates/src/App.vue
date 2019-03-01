<template>
  <div id="app">
    <header>
    <Test></Test>
    </header>
    <div style="width:550px;margin: 0 auto;">
        <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
          <el-form-item label="用户名" prop="username">
            <el-input v-model="ruleForm.username"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="userpassword">
            <el-input v-model="ruleForm.userpassword"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm')">立即创建</el-button>
            <el-button @click="resetForm('ruleForm')">重置</el-button>
          </el-form-item>
        </el-form>

    </div>
    <h1>{{ruleForm.username}}</h1>
    <h1>{{ruleForm.userpassword}}</h1>
    <div style="width:400px;text-align: center;">
    <router-view/>
    </div>
    <footer>
      <h1>now you see me</h1>
    </footer>

  </div>

</template>

<script>

import Test from './components/test.vue'
export default {
  components:{
    Test,
  },
  data() {
      return {
        ruleForm: {
          username: '',
          userpassword: '',
        },
        rules: {
          username: [
            { required: true, message: '请输入用户名', trigger: 'blur' },
            { min: 1, max: 20, message: '长度在 1 到 20 个字符', trigger: 'blur' }
          ],
          userpassword: [
            { required: true, message: '请输入密码', trigger: 'blur' },
            { min: 6, max: 15, message: '长度在 6 到 15 个字符', trigger: 'blur' }

          ],
        }
      };
    },
  methods: {
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            alert(this.ruleForm);
            var vm = this;
            var arr, reg = new RegExp("(^| )" + "csrftoken" + "=([^;]*)(;|$)");
            arr = document.cookie.match(reg)[2]
            alert(arr)
            this.$ajax({
              method: 'post',
              url:'http://localhost:8000/user/login/',
              data :{
                username: this.ruleForm.username,
                password: this.ruleForm.userpassword
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
              window.location = '/projects'  //登录成功后跳转到home页面
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
      }
    },
  name: 'App'
}


</script>


<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
</style>
