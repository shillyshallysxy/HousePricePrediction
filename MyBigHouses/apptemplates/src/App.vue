<template>
  <div id="app">
    <header>
    <HeadNav></HeadNav>
    </header>
    <div style="width:400px;text-align: center;margin:0 auto">

    <router-view/>
    </div>
    <footer>
    </footer>

  </div>

</template>

<script>

import HeadNav from './components/HeadNav.vue'
export default {
  components:{
    HeadNav,
  },

  name: 'App'
}


</script>


<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
</style>
