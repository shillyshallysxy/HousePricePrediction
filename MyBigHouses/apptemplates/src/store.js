import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex);


export default new Vuex.Store({
  state:{
    isLogin : false,
    UserInfo:{
      username : '',
    },
    area:{
			city: "suzhou",
			area: "工业园区"
		}
  },
  mutations:{
    change_isLogin(state,username){

      state.isLogin = true,
      state.UserInfo.username = username
    },

    change_LoginOut(state){
      state.isLogin = false,
      state.UserInfo.username = ''
    }
  },
  actions:{

  },
  getters:{
    getIsLogin: function(state){
      return state.isLogin
    },
    getUserInfo: function(state){
      return state.UserInfo
    }
  }
})
