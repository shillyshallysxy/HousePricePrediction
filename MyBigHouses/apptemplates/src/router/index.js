import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import MainPage from '@/components/MainPage'
import Register from '@/components/Register'
import PriceDemo from '@/components/PriceDemo'
Vue.use(Router)

export default new Router({
  mode:'history',
  routes: [
    {
      path: '/',
      name: 'MainPage',
      component: MainPage
    },
    {
      path: '/user/login',
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
			name: 'PriceDemo',
			component: PriceDemo,
			meta:{
        requireLogin: true
      }
		}

  ]
})
