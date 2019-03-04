import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import MainPage from '@/components/MainPage'
import Register from '@/components/Register'
Vue.use(Router)

export default new Router({
<<<<<<< HEAD
  mode: 'history',
=======
  mode:'history',
>>>>>>> 4db98fe6b64135ccd9a27ccdb2e9eb5ed2bad2a2
  routes: [
    {
      path: '/',
      name: 'MainPage',
      component: MainPage
    },
    {
      path: '/user/login',
      name: 'HelloWorld',
      component: Login
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    }

  ]
})
