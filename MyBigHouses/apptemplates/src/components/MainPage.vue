<template>
    <div v-bind:class="{body: true}" style="min-width: 1350px;">
        <div v-bind:class="{background: true}">
          <div v-bind:class="{price: true}">
						<div v-bind:class="{city:true}">
							<h2 style="font-family: 黑体;color: black;text-align: center;">
								苏州
							<!--todo这里的city后台传值进来-->
							</h2>
							<div>
								<h4 style="font-family:times new roman;color: black;text-align: center;">
									SuZhou
									<!--todo这里的city后台传值进来-->
								</h4>
								<div style="margin-top: 5px;text-align: center;font-size: 5px;">
									<h1 style="font-family:times new roman;color: black;text-align: center;">
										均价:1.64w
										<!--todo这里的价格后台传值进来-->
									</h1>
									<h4 style="font-family: 黑体;color: black;text-align: center;">
										来源最近15天数据
									</h4>
								</div>
							</div>
						</div>
          </div>
        </div>
		
		<!--bar代码-->
		<div style="background-color: #009688;width: 100%;height: 150px;min-width: 1350px;">
			<div style="width: 20%;height: 60px;margin-top: 45px;margin-left: 7.5%;float: left;">
				<img src="../assets/logo1.png" style="max-height: 40px;float: left;margin-left: 100px;margin-top: 10px;"/>
				<p style="font-size: 15px;color: white;font-weight: 500;margin-left: 10px;margin-top: 10px;">
					当前房价
				</p>
				<p style="font-size: 10px;color: white;font-weight: 500;margin-left: 10px;">
					Current house price
				</p>
			</div>
			<div style="width: 20%;height: 60px;margin-top: 45px;margin-left: 7.5%;float: left;">
				<img src="../assets/logo1.png" style="max-height: 40px;float: left;margin-left: 100px;margin-top: 10px;"/>
				<p style="font-size: 15px;color: white;font-weight: 500;margin-left: 10px;margin-top: 10px;">
					房价预测
				</p>
				<p style="font-size: 10px;color: white;font-weight: 500;margin-left: 10px;">
					House price prediction
				</p>
			</div>
			<div style="width: 20%;height: 60px;margin-top: 45px;margin-left: 7.5%;float: left;">
				<img src="../assets/logo1.png" style="max-height: 40px;float: left;margin-left: 100px;margin-top: 10px;"/>
				<p style="font-size: 15px;color: white;font-weight: 500;margin-left: 10px;margin-top: 10px;">
					挑好房
				</p>
				<p style="font-size: 10px;color: white;font-weight: 500;margin-left: 10px;">
					Selete ideal house
				</p>
			</div>
		</div>
		
		<!--精品二手房代码-->
		<div style="background-color: white;width: 100%;height: 800px;margin: 0;padding: 0;display:block;">
			<div style="background-color: white;width: 70%;margin-left: 15%;height: 800px;">	
				<div style="width: 100%;height: 100px;min-width: 920px;">
					<p style="font-size: 25px;margin-left: 5%;float: left;margin-top: 55px;"><b>精选好房</b>，为你而选</p>
					<p style="font-size: 15px;float:right;margin-right: 5%;margin-top: 55px;">更多好房</p>
				</div>
				<div style="width: 100%;height: 300px;float: left; min-width: 920px;">
					<div v-bind:class="{erShouFang: true}">
						<img src="../assets/2.jpg" style="max-width: 180px;height: 120px;background-size: cover"/>
						<p v-bind:class="{erShouName: true}" style="color: #009688;">望京新城1</p>
						<p v-bind:class="{erShouName: true}" style="color: darkgray;">望京新城 3室1厅 东南</p>
						<p style="display: inline-block;font-size: 15px;font-weight: 500;left: 5px;margin-right: 30px;">96.47平米</p>
						<p style="display: inline-block;font-size: 15px;font-weight: 500;color: red;right: 5px;">650万</p>
					</div>
					<div v-bind:class="{erShouFang: true}">
						<img src="../assets/2.jpg" style="max-width: 180px;height: 120px;background-size: cover"/>
						<p v-bind:class="{erShouName: true}" style="color: #009688;">望京新城1</p>
						<p v-bind:class="{erShouName: true}" style="color: darkgray;">望京新城 3室1厅 东南</p>
						<p style="display: inline-block;font-size: 15px;font-weight: 500;left: 5px;margin-right: 30px;">96.47平米</p>
						<p style="display: inline-block;font-size: 15px;font-weight: 500;color: red;right: 5px;">650万</p>
					</div>
					<div v-bind:class="{erShouFang: true}">
						<img src="../assets/2.jpg" style="max-width: 180px;height: 120px;background-size: cover"/>
						<p v-bind:class="{erShouName: true}" style="color: #009688;">望京新城1</p>
						<p v-bind:class="{erShouName: true}" style="color: darkgray;">望京新城 3室1厅 东南</p>
						<p style="display: inline-block;font-size: 15px;font-weight: 500;left: 5px;margin-right: 30px;">96.47平米</p>
						<p style="display: inline-block;font-size: 15px;font-weight: 500;color: red;right: 5px;">650万</p>
					</div>
					<div v-bind:class="{erShouFang: true}">
						<img src="../assets/2.jpg" style="max-width: 180px;height: 120px;background-size: cover"/>
						<p v-bind:class="{erShouName: true}" style="color: #009688;">望京新城1</p>
						<p v-bind:class="{erShouName: true}" style="color: darkgray;">望京新城 3室1厅 东南</p>
						<p style="display: inline-block;font-size: 15px;font-weight: 500;left: 5px;margin-right: 30px;">96.47平米</p>
						<p style="display: inline-block;font-size: 15px;font-weight: 500;color: red;right: 5px;">650万</p>
					</div>
				</div>		
				<div style="width: 100%;height: 50px;min-width: 920px;">
					<p style="font-size: 25px;margin-left: 5%;float: left;margin-top: 5px;"><b>投资之最</b>，未来可期</p>
					<p style="font-size: 15px;float:right;margin-right: 5%;margin-top: 5px;">更多好房</p>
				</div>
				<div style="width: 100%;height: 300px;float: left;min-width: 920px;">
					<div v-bind:class="{erShouFang: true}">
						<img src="../assets/2.jpg" style="max-width: 180px;height: 120px;background-size: cover"/>
						<p v-bind:class="{erShouName: true}" style="color: #009688;">望京新城1</p>
						<p v-bind:class="{erShouName: true}" style="color: darkgray;">望京新城 3室1厅 东南</p>
						<p style="display: inline-block;font-size: 15px;font-weight: 500;left: 5px;margin-right: 30px;">96.47平米</p>
						<p style="display: inline-block;font-size: 15px;font-weight: 500;color: red;right: 5px;">650万</p>
					</div>
					<div v-bind:class="{erShouFang: true}">
						<img src="../assets/2.jpg" style="max-width: 180px;height: 120px;background-size: cover"/>
						<p v-bind:class="{erShouName: true}" style="color: #009688;">望京新城1</p>
						<p v-bind:class="{erShouName: true}" style="color: darkgray;">望京新城 3室1厅 东南</p>
						<p style="display: inline-block;font-size: 15px;font-weight: 500;left: 5px;margin-right: 30px;">96.47平米</p>
						<p style="display: inline-block;font-size: 15px;font-weight: 500;color: red;right: 5px;">650万</p>
					</div>
					<div v-bind:class="{erShouFang: true}">
						<img src="../assets/2.jpg" style="max-width: 180px;height: 120px;background-size: cover"/>
						<p v-bind:class="{erShouName: true}" style="color: #009688;">望京新城1</p>
						<p v-bind:class="{erShouName: true}" style="color: darkgray;">望京新城 3室1厅 东南</p>
						<p style="display: inline-block;font-size: 15px;font-weight: 500;left: 5px;margin-right: 30px;">96.47平米</p>
						<p style="display: inline-block;font-size: 15px;font-weight: 500;color: red;right: 5px;">650万</p>
					</div>
					<div v-bind:class="{erShouFang: true}">
						<img src="../assets/2.jpg" style="max-width: 180px;height: 120px;background-size: cover"/>
						<p v-bind:class="{erShouName: true}" style="color: #009688;">望京新城1</p>
						<p v-bind:class="{erShouName: true}" style="color: darkgray;">望京新城 3室1厅 东南</p>
						<p style="display: inline-block;font-size: 15px;font-weight: 500;left: 5px;margin-right: 30px;">96.47平米</p>
						<p style="display: inline-block;font-size: 15px;font-weight: 500;color: red;right: 5px;">650万</p>
					</div>
				</div>	
			</div>
		</div>
		
		<!--房价趋势代码-->
		<div style="background-color: #E8E8E8;width: 100%;height: 320px;margin: 0;padding: 0;display:block;min-width: 1300px;">
			<div style="width: 100%;height: 100px;">
				<p style="font-size: 25px;margin-left: 20%;float: left;margin-top: 25px;"><b>房价走势</b>，以史为鉴</p>
			</div>
			<div style="background-color: #0000FF;width: 320px;height: 200px;background-size: 100% 100%;display: inline-block;margin-right: 10%;"></div>
			<div style="background-color: red;width: 320px;height: 200px;background-size: 100% 100%;display: inline-block;"></div>
			
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
  height:100%;
  width:100%;
  padding:0px;
  margin-top:12px;
  display:block;
  position:relative;
  background-position-y: 0px
}
.background {
  width:100%;
  height:700px;
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
	margin-top:20px;
	z-index:2;
	font-family: "黑体";
}
.erShouFang{
	width: 180px ;
	height: 240px;
	background-color: white;
	border: 1px solid lightgray;
	z-index: 1;
	float: left;
	margin-left: 5%;
	
}
.erShouName{
	font-size: 12px;
	font-family: "黑体";
	font-weight: 500;
	text-align: left;
	margin-left: 10px;
}
</style>
