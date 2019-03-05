<template>
    <div v-bind:class="{body: true}">
        <div v-bind:class="{background: true}">
          <div v-bind:class="{price: true}">
						<div v-bind:class="{city:true}">
							<h2 style="font-family:Georgia;color: black;text-align: center;">苏州
							<!--todo这里的city后台传值进来-->
							</h2>
							<div>
								<h4 style="font-family:times new roman;color: black;text-align: center;">
									SuZhou
									<!--todo这里的city后台传值进来-->
								</h4>
								<div style="margin-top: 5px;text-align: center;font-size: 5px;">
									<h1 style="font-family:Georgia;color: black;text-align: center;">
										均价:3.64w
										<!--todo这里的价格后台传值进来-->
									</h1>
										来源最近15天数据
								</div>
							</div>
						</div>
          </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
			return{
				
			}
    },
    methods: {

    }
}
</script>

<style>
.body{
  height:700px;
  width:100%;
  padding:0px;
  margin:0px;
  display:block;
  position:relative;
  background-position-y: 0px
}
.background {
  width:100%;
  height:100%;
  background-image:url(../assets/main_bg.jpg);
  background-repeat: no-repeat;
  background-size:100% 100%;
 }
.price{
  width:200px;
  height:200px;
  background-color:white;
	margin-right: 150px;
	margin-top: 200px;
  float:right;
	filter:alpha(Opacity=70);-moz-opacity:0.7;opacity: 0.7;
	z-index:1;
}
.city{
	width: 200px;
	height: 150px;
	margin-top: 20px;
	z-index:2;

}
</style>
