    <template>
    <el-menu router :default-active="$route.path" class="el-menu-demo" mode="horizontal" @select="handleSelect" background-color="#545c64" text-color="#fff" active-text-color="#ffd04b">

        <el-menu-item index="/user/login" >登陆</el-menu-item>

        <el-menu-item v-else>注销</el-menu-item>
        <el-submenu index="2">
            <template slot="title">我的工作台</template>
            <el-menu-item index="2-1">选项1</el-menu-item>
            <el-menu-item index="2-2">选项2</el-menu-item>
            <el-menu-item index="2-3">选项3</el-menu-item>
        </el-submenu>
        <el-menu-item index="/price_condition">{{data.isLogin}}</el-menu-item>
    </el-menu>
</template>

<script>
import store from '@/store'
export default {
		store,
        data() {
            return {
                activeIndex: '1',
                activeIndex2: '1',
                isLogin: store.state.UserInfo.username

            };
        },
		mounted(){
			var username = sessionStorage.getItem('username')
				
			if(username!=''){
				console.log(store.state.isLogin)
			}
			
			},
        methods: {

            handleSelect(key, keyPath) {
                console.log(key, keyPath);
            }
        }
    }
</script>

<style scoped>


</style>
