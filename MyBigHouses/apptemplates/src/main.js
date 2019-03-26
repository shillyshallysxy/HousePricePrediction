// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import axios from 'axios'
import VueHighCharts from 'vue-highcharts'
import Highcharts from 'highcharts'
import store from '@/store'
import BMap from 'BMap';
import iView from 'iview';
import 'iview/dist/styles/iview.css'
import global_ from './components/Global'//引用文件
import {
		getCookie,
		setCookie,
		delCookie
	} from '@/utils/utils'
//import {Message} from 'iview'
//使用iView插件
Vue.use(iView) 
/* 使用element-ui插件 */
Vue.use(ElementUI)
Vue.config.productionTip = false
Vue.prototype.$ajax = axios
//Vue.prototype.$Message = Message
Vue.use(VueHighCharts,{Highcharts})
//挂载ip全局变量
Vue.prototype.GLOBAL = global_//挂载到Vue实例上面
/*
main.js的文件调用顺序：
（1）确定将被挂载的元素  el:'#app'
（2）注册组件，并选择其中用于替换挂载元素的模版组件（<App/>）
（3）注入路由器router：
    1. 模版组件（app.vue）中有<router-view/>,将在其中渲染匹配到的组件
    2. 注入路由时指定router文件夹，指定文件夹下所有的routes
    3. router文件夹下此时只有index.js文件，其中routes[]规定了文件地址及其url地址映射
    4. 根据文件地址，载入组件，组件被渲染在<router-view>中，被显示在index.html中
*/
//进入每个页面前的钩子函数
router.beforeEach((to, from ,next) =>{
	//获取是否登陆、用户名信息
  let flag = getCookie("Flag")
  let username = getCookie("username")
  //获取省份，城市，地区的中文和拼音
	let province = localStorage.getItem("province")
	let city = localStorage.getItem("city")
	let area = localStorage.getItem("area")
	let street = localStorage.getItem("street")
	let province_eng = localStorage.getItem("province_eng")
	let city_eng = localStorage.getItem("city_eng")
	let area_eng = localStorage.getItem("area_eng")
	let street_eng = localStorage.getItem("street_eng")
	//如果省份不为空，则将省份城市区信息存储到store
	if(province!=null){
		store.state.area.province = province
		store.state.area.city = city
		store.state.area.area = area
		store.state.area.street = street
		store.state.area_eng.province = province_eng
		store.state.area_eng.city = city_eng
		store.state.area_eng.area = area_eng
		store.state.area_eng.street = street_eng
		

	}
// 	else{
// 		//获取当前城市
// 		var location = getCurrentCity()
// 		//写入localStorage
// 		localStorage.setItem("province", location[0])
// 		localStorage.setItem("city", location[1])
// 	}

  if(flag==='isLogin'){
	  //如果已经登陆，且去的市登陆界面，则跳转到主页
		if(to.path == '/register'){
			next('/')
		}else{
			//设置store中的登陆为true
			store.state.isLogin = true
			store.state.UserInfo.username = username
			next()
		}   
  }else{
	  //如果未登陆，且去的页面需要登陆，则跳转到登陆页面
    store.state.isLogin =false
    if(to.meta.requireLogin){
      next({path: '/login'})
      iView.Message.info('请先登录')
    }else{
      next()
    }
  }

})

// function getCurrentCity() {    //定义获取城市方法
//   const geolocation = new BMap.Geolocation();
//   let self = this
// 	let city
// 	let province
//   geolocation.getCurrentPosition(function getinfo(position) {
// 		city = position.address.city;             //获取城市信息
// 		province = position.address.province;    //获取省份信息
// 		console.log(city+":"+province)
// // 		store.state.area.city = city
// // 		store.state.area.province = province
//     // sessionStorage.setItem('currentCity', city.substr(0, city.length - 1))
//   }, function (e) {
//   }, {provider: 'baidu'});
// 	let location= []
// 	location.push(city)
// 	location.push(province)
// 	return location
// };

/* eslint-disable no-new */
new Vue({
  /* 为实例提供挂载的文件*/
  el: '#app',
  /* 指向引入文件中的routes:[]*/
  router,
  /* 注册哪些组件，需在顶部引入文件*/
  components: { App },
  /* 替换挂载元素的模版组件*/
  template: '<App/>',
// 	mounted() {
// 		getCurrentCity()
// 	}
})


