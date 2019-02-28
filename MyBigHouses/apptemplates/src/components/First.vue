</template>
    <div><h1>
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" class="demo-ruleForm loginFrom">
      <h1 style="font-size: 1.5rem;color: #fff;font-weight: bold;padding: 1rem 0;">登陆</h1>
      <el-form-item >
        <el-input placeholder="账号"  v-model="ruleForm.userName"></el-input>
      </el-form-item>
      <el-form-item>
        <el-input  type="password" v-model="ruleForm.password" placeholder="密码"></el-input>
      </el-form-item>
      <div style="padding: 1rem 0 2rem 0;" class="clear">
        <span class="lf" style="color:#0489cc;">帮助</span>
        <div class="rt">
          <el-checkbox v-model="checked" style="color:#a0a0a0;">一周内自动登录</el-checkbox>
          <span @click="clearCookie" style="cursor: pointer;color: #f19149;font-size: 0.75rem;margin-left: 5px;">忘记密码？</span>
        </div>
      </div>
      <el-button type="primary" @click="submitForm('ruleForm')" style="width: 100%;">登陆</el-button>
    </el-form>
   </h1></div>
</template>

<script>
export deflaut {
    name:'First.vue',
    data(){
        return{
            message:'welcome'
        }
    }
}
</script>

<style scoped>


</style>
