import Vue from 'vue'
import Vuex from 'vuex'
import global_ from '@/components/Global'
import iView from 'iview'
import axios from 'axios'
Vue.use(Vuex);


export default new Vuex.Store({
	state: {
		isLogin: false,//是否登陆
		UserInfo: {
			username: '',//用户名
		},
		//省份、城市、区、街道的中文
		area: {
			province: "江苏省",
			city: "无锡",
			area: "",
			street: ""
		},
		//省份、城市、区、街道的英文
		area_eng: {
			province: "jiangsu",
			city: "wuxi",
			area: "",
			street: "",
			average_price: '1.634',
		}
	},
	mutations: {
		//修改登陆状态
		change_isLogin(state, username) {

			state.isLogin = true,
				state.UserInfo.username = username
		},
		//退出登陆
		change_LoginOut(state) {
			state.isLogin = false,
				state.UserInfo.username = ''
		},
		//修改所在地信息
		change_AreaInfo(state, area) {
			// console.log("更改了城市")
			state.area.province = area['province'],
				state.area.city = area['city'],
				state.area.area = area['area']
			state.area.street = area['street']
			localStorage.setItem("province", area["province"])
			localStorage.setItem("city", area['city'])
			localStorage.setItem("area", area['area'])
			localStorage.setItem("street", area["street"])
			state.area_eng.province = area['province_eng'],
				state.area_eng.city = area['city_eng'],
				state.area_eng.area = area['area_eng']
			state.area_eng.street = area['street_eng']
			localStorage.setItem("province_eng", area["province_eng"])
			localStorage.setItem("city_eng", area['city_eng'])
			localStorage.setItem("area_eng", area['area_eng'])
			localStorage.setItem("street_eng", area["street_eng"])
			
			
		}
	},
	actions: {

	},
	getters: {
		//获取信息的方法
		getIsLogin: function(state) {
			return state.isLogin
		},
		getUserInfo: function(state) {
			return state.UserInfo
		},
		getAreaInfo: function(state) {
			return state.area
		}
	}
})
