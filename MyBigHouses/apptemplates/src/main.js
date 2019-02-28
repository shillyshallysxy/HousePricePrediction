// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

/* 使用element-ui插件 */
Vue.use(ElementUI)
Vue.config.productionTip = false

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

/* eslint-disable no-new */
new Vue({
  /* 为实例提供挂载的文件*/
  el: '#app',
  /* 指向引入文件中的routes:[]*/
  router,
  /* 注册哪些组件，需在顶部引入文件*/
  components: { App },
  /* 替换挂载元素的模版组件*/
  template: '<App/>'
})

