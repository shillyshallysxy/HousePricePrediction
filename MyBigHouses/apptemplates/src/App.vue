<template>
  <div id="app">
    <header>
    <HeadNav></HeadNav>
    </header>
    <div style="width:100%;text-align: center;margin:0 auto">

    <router-view/>
    </div>
    <footer>
			<FootNav></FootNav>
    </footer>

  </div>

</template>

<script>

import HeadNav from './components/HeadNav.vue'
import FootNav from './components/FootNav.vue'
export default {
  components:{
    HeadNav,
		FootNav
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
