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
			province: "江苏省",
			city: "苏州",
			area: "吴中区",
			street: ""
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
    },
		change_AreaInfo(state, area){
			state.area.province = area['province'],
			state.area.city = area['city'],
			state.area.area = area['area']
			state.area.street = area['street']
			localStorage.setItem("province", area["province"])
			localStorage.setItem("city", area['city'])
			localStorage.setItem("area", area['area'])
			localStorage.setItem("street", area["street"])
			
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
    },
		getAreaInfo: function(state){
			return state.area
		}
  }
})
