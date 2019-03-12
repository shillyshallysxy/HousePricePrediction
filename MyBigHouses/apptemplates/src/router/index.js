import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import MainPage from '@/components/MainPage'
import Register from '@/components/Register'
import PriceCharts from '@/components/PriceCharts'
import AreaSelect from '@/components/AreaSelect'
import UserInfo from '@/components/UserInfo'
import SelectHouse from '@/components/SelectHouse'
import ItemPage from '@/components/ItemPage'
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
      name: 'HelloWorld',
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
			path: '/SelectHouse',
			name: 'SelectHouse',
			component: SelectHouse,
			meta:{
				requireLogin: false
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
		

  ]
})

