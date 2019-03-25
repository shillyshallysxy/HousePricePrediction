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
    {
      path: '/',
      name: 'MainPage',
      component: MainPage,
      meta:{
        requireLogin: false
      }
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
      meta:{
        requireLogin: false
      }
    },
    {
      path: '/register',
      name: 'register',
      component: Register,
      meta:{
        requireLogin: false
      }
    },
		{
			path: '/price_condition',
			name: 'PriceCharts',
			component: PriceCharts,
			meta:{
        requireLogin: true
      }
		},
		{
			path: '/AreaSelect',
			name: 'AreaSelect',
			component: AreaSelect,
			meta:{
		    requireLogin: false
		  }
		},
		{
			path: '/UserInfo',
			name: 'UserInfo',
			component: UserInfo,
			meta:{
				requireLogin: true
			}
		},
		{
			path: '/ItemPage',
			name: 'ItemPage',
			component: ItemPage,
			meta:{
				requireLogin: false
			}
		},
		{
			path: '/PricePredict',
			name: 'PricePredict',
			component: PricePredict,
			meta:{
				requireLogin:true
			}
		},
		{
			path: '/HouseChoosing',
			name: 'HouseChoosing',
			component: HouseChoosing,
			meta: {
				requireLogin:true
			}
		},
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

