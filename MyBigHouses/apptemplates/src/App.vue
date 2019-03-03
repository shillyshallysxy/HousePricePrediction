<template>
  <div id="app">
    <header>
    <Test></Test>
    </header>

    <div style="width:400px;text-align: center;">
    <router-view/>
    </div>
    <footer>
    </footer>

  </div>

</template>

<script>

import Test from './components/test.vue'
export default {
  components:{
    Test,
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
