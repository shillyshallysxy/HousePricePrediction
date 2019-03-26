import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import MainPage from '@/components/MainPage'
import Register from '@/components/Register'
import PriceCharts from '@/components/PriceCharts'
import AreaSelect from '@/components/AreaSelect'
import UserInfo from '@/components/UserInfo'
import ItemPage from '@/components/ItemPage'
import PricePredict from '@/components/PricePredict'
import HouseChoosing from '@/components/HouseChoosing'
import Search from '@/components/Search'
Vue.use(Router)

export default new Router({
  mode:'history',
  routes: [
	  //主页
    {
      path: '/',
      name: 'MainPage',
      component: MainPage,
      meta:{
        requireLogin: false
      }
    },
	//登陆页面
    {
      path: '/login',
      name: 'login',
      component: Login,
      meta:{
        requireLogin: false
      }
    },
	//注册页面
    {
      path: '/register',
      name: 'register',
      component: Register,
      meta:{
        requireLogin: false
      }
    },
	//房价走势页面
		{
			path: '/price_condition',
			name: 'PriceCharts',
			component: PriceCharts,
			meta:{
        requireLogin: true
      }
		},
		//地区选择页面
		{
			path: '/AreaSelect',
			name: 'AreaSelect',
			component: AreaSelect,
			meta:{
		    requireLogin: false
		  }
		},
		//用户信息页面
		{
			path: '/UserInfo',
			name: 'UserInfo',
			component: UserInfo,
			meta:{
				requireLogin: true
			}
		},
		//房源详情页面
		{
			path: '/ItemPage',
			name: 'ItemPage',
			component: ItemPage,
			meta:{
				requireLogin: false
			}
		},
		//房价预测页面
		{
			path: '/PricePredict',
			name: 'PricePredict',
			component: PricePredict,
			meta:{
				requireLogin:true
			}
		},
		//选房页面
		{
			path: '/HouseChoosing',
			name: 'HouseChoosing',
			component: HouseChoosing,
			meta: {
				requireLogin:true
			}
		},
		//搜索页面
		{
			path: '/Search',
			name: 'Search',
			component: Search,
			meta:{
				requireLogin:false
			}
		}
		

  ]
})

