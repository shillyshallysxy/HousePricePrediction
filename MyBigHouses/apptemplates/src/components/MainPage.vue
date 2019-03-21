<template>
	<div class="body" style="min-width: 1050px;">		
		
		<div class="swiper-container">
			<div class="topic_line">
				<p style="font-size: 36px;color: white;font-weight: 500;font-family: arial;">
					House only for you.
				</p>				
			</div>
			<div class="search_line">
				<div class="search_block">
					<el-input v-model="search" clearable></el-input>
				</div>
				<button class="search_button">搜索</button>
			</div>
			<div class="price">
				<div class="city">
					<h1 style="font-family: 黑体;color: black;text-align: center;font-size: 32px;">
						{{city_name_cn}}
					</h1>
					<h3 style="font-family:times new roman;color: black;text-align: center;font-size: 18px;">
						{{city_name_en}}
					</h3>
				</div>
				<div class="price_body">
					<h1 style="font-family:times new roman;color: black;text-align: center;font-size: 32px;">
						均价:{{average_price}}w
					</h1>
				</div>
				<div style="margin-top: 20px;">
					<h4 style="font-family: 黑体;color: black;text-align: center;">
						来源最近15天数据
					</h4>
				</div>
			</div>
			<div class="swiper-wrapper">
		        <div class="swiper-slide" v-for="item in listImg">
		        	<img :src="item.url"/>
		        </div>
		    </div>	
		    <div class="swiper-pagination swiper-pagination-white"></div>
		</div>

		<!--bar代码-->
		<div style="background-color: #009688;width: 100%;height: 150px;min-width: 1050px;">
			<div style="width: 26%;height: 60px;margin-top: 45px;margin-left: 5%;float: left;">
				<img src="../assets/logo1.png" style="max-height: 40px;float: left;margin-left: 100px;margin-top: 10px;" />
				<p style="font-size: 15px;color: white;font-weight: 500;margin-top: 10px;">
					当前房价
				</p>
				<p style="font-size: 10px;color: white;font-weight: 500;">
					Current house price
				</p>
			</div>
			<div style="width: 26%;height: 60px;margin-top: 45px;margin-left: 5%;float: left;">
				<img src="../assets/logo1.png" style="max-height: 40px;float: left;margin-top: 10px;" />
				<p style="font-size: 15px;color: white;font-weight: 500;margin-top: 10px;">
					房价预测
				</p>
				<p style="font-size: 10px;color: white;font-weight: 500;margin-left: 10px;">
					House price prediction
				</p>
			</div>
			<div style="width: 26%;height: 60px;margin-top: 45px;margin-left: 5%;float: left;">
				<img src="../assets/logo1.png" style="max-height: 40px;float: left;margin-top: 10px;" />
				<p style="font-size: 15px;color: white;font-weight: 500;margin-top: 10px;">
					挑好房
				</p>
				<p style="font-size: 10px;color: white;font-weight: 500;margin-left: 10px;">
					Selete ideal house
				</p>
			</div>
		</div>

		<!--精品二手房代码-->
		<div style="background-color: white;width: 100%;height: 750px;margin: 0;padding: 0;display:block;min-width: 1050px;">
			<div style="width: 100%;height: 750px;clear: both;padding-top: 1px;padding-left: 50%;background-attachment: fixed;-webkit-background-size: cover;-moz-background-size: cover;-o-background-size: cover;background-size: cover;">
				<div style="width: 100%;height: 100px;min-width: 950px;margin-left: -475px;">
					<p style="font-size: 25px;margin-left: 5%;float: left;margin-top: 55px;"><b>精选好房</b>，为你而选</p>
					<p style="font-size: 15px;float:right;margin-right: 5%;margin-top: 55px;">更多好房</p>
				</div>
				<div style="width: 100%;height: 300px;float: left; min-width: 950px;margin-left: -475px;">
					<el-row>
						<el-col :span="8" v-for="(o, index) in ShowHouse" :key="o.id" :offset="index > 0 ? 2 : 0" style="margin-bottom: 2.5rem;margin-left:46px ;width: 182px;height: 250px;">
							<el-card :body-style="{ padding: '0px', height:'250px'}" style="width: 180px;">
								<img :src="o.pic_src" class="image">
								<div style="padding-top: 10px;padding-left: 20px;padding-right: 20px;">
									<div style="width: 140px;height: 20px;">
										<p class="erShouName" style="color: #009688;">{{o.name}}</p>
									</div>
									<div style="width: 120px;margin-left: 10px;height: 40px;">
										<p class="erShouName" style="color: darkgray;margin-top:5px;font-size: 12px;display: -webkit-box;-webkit-box-orient: vertical;-webkit-line-clamp: 2;overflow: hidden;">{{o.detail}}</p>
									</div>
									<div style="width: 140px;height: 20px;float: left;">
										<p style="display: inline-block;font-size: 15px;font-weight: 500;float: left;">{{o.area}}平米</p>
										<p style="display: inline-block;font-size: 15px;font-weight: 500;float: left;color: red;margin-left: 10px;">{{o.price}}万</p>							
									</div>
									<div style="width: 140px;float: right;">
										<el-button type="text" class="button" style="margin-top: 5px;padding: 0; float: right;" data-index="o.id"
										 @click.native="go_to_detail_page(o.id)">查看详情</el-button>
									</div>
								</div>
							</el-card>
						</el-col>
					</el-row>
				</div>

				<div style="width: 100%;height: 50px;min-width: 950px;margin-left: -475px;">
					<p style="font-size: 25px;margin-left: 5%;float: left;margin-top: 5px;"><b>投资之最</b>，未来可期</p>
					<p style="font-size: 15px;float:right;margin-right: 5%;margin-top: 5px;">更多好房</p>
				</div>
				<div style="width: 100%;height: 300px;float: left;min-width: 950px;margin-left: -475px;margin-top: 18px;">
					<el-row>
						<el-col :span="8" v-for="(o, index) in ShowHouse2" :key="o.id" :offset="index > 0 ? 2 : 0" style="margin-bottom: 2.5rem;margin-left:46px ;width: 182px;height: 250px;">
							<el-card :body-style="{ padding: '0px', height:'250px'}" style="width: 180px;">
								<img :src="o.pic_src" class="image">
								<div style="padding-top: 10px;padding-left: 20px;padding-right: 20px;">
									<div style="width: 140px;height: 20px;">
										<p class="erShouName" style="color: #009688;">{{o.name}}</p>
									</div>
									<div style="width: 120px;margin-left: 10px;height: 40px;">
										<p class="erShouName" style="color: darkgray;margin-top:5px;font-size: 12px;display: -webkit-box;-webkit-box-orient: vertical;-webkit-line-clamp: 2;overflow: hidden;">{{o.detail}}</p>
									</div>
									<div style="width: 140px;height: 20px;float: left;">
										<p style="display: inline-block;font-size: 15px;font-weight: 500;float: left;">{{o.area}}平米</p>
										<p style="display: inline-block;font-size: 15px;font-weight: 500;float: left;color: red;margin-left: 10px;">{{o.price}}万</p>							
									</div>
									<el-button type="text" class="button" style="margin-top: 10px;padding: 0; float: right;" @click.native="go_to_detail_page(o.id)">查看详情</el-button>
								</div>
							</el-card>
						</el-col>
					</el-row>

				</div>
			</div>
		</div>

		<!--房价趋势代码-->
		<div style="background-color: #E8E8E8;width: 100%;height: 320px;margin: 0;padding: 0;display:block;min-width: 950px;">
			<div style="width: 100%;height: 320px;clear: both;padding-top: 1px;padding-left: 50%;background-attachment: fixed;-webkit-background-size: cover;-moz-background-size: cover;-o-background-size: cover;background-size: cover;">
				<div style="width: 100%;height: 100px;margin-left: -425px;">
					<p style="font-size: 25px;float: left;margin-top: 25px;"><b>房价走势</b>，以史为鉴</p>
				</div>
				<div style="background-color: #0000FF;width: 320px;height: 200px;background-size: 100% 100%;float: left;margin-left: -425px;"></div>
				<div style="background-color: red;width: 320px;height: 200px;background-size: 100% 100%;float: left;margin-left: 100px;"></div>
			</div>
		</div>
	</div>
</template>

<script>
	import store from '@/store'
	import global_ from '@/components/Global'
	import iView from 'iview'
	import Swiper from 'swiper';
	import 'swiper/dist/css/swiper.min.css';
	export default {
		data() {
			return {
				city_name_cn: '苏州',
				city_name_en: 'SuZhou',
				average_price: '1.64',
				ShowHouse: [],
				ShowHouse2: [],
				search: '',
				//图片路径
				listImg:[
					{url:require('../../src/assets/main_bg.jpg')},
					{url:'../../static/images/2.jpg'},
					{url:require('../../src/assets/login_back.jpg')}	
				]
			}
		},
		mounted() {
			this.city_name_cn = store.state.area.city
			this.city_name_en = store.state.area_eng.city
			this.get_mainpage_info()
			var _this = this
			_this.$ajax({
				method: 'get',
				url: global_.IpUrl + '/house/price/' + this.get_city() + '/overview',
			}).then(function(response) {
				var house_info = response.data.data
				for (var i = 0; i <= 3; i++) {
					var temp1 = {}
					temp1['id'] = house_info[i].id
					var pic = house_info[i].img_url
					temp1['pic_src'] = pic
					temp1['name'] = house_info[i].garden
					temp1['detail'] = house_info[i].description
					temp1['area'] = house_info[i].area
					temp1['price'] = house_info[i].total_price
					_this.ShowHouse.push(temp1)
				}
				for (var i = 4; i <= 7; i++) {
					var temp1 = {}
					temp1['id'] = house_info[i].id
					var pic = house_info[i].img_url
					temp1['pic_src'] = pic
					temp1['name'] = house_info[i].garden
					temp1['detail'] = house_info[i].description
					temp1['area'] = house_info[i].area
					temp1['price'] = house_info[i].total_price
					_this.ShowHouse2.push(temp1)
				}
				
			})
			
			console.log('mounted', this)
			var mySwiper = new Swiper ('.swiper-container', {
			    loop: true, 
			    pagination: {
			      el: '.swiper-pagination',
			    },    
			    // 如果需要前进后退按钮
			    navigation: {
			      nextEl: '.swiper-button-next',
			      prevEl: '.swiper-button-prev',
			    },
			    autoplay: {
			    disableOnInteraction: false,
			  },
				speed:800,
			})  
		},
		methods: {
			go_to_detail_page(id) {
				this.$router.push({
					path: 'ItemPage',
					query: {
						HouseId: id
					}
				})
			},
			get_city() {
				console.log("获取了城市")
				return store.state.area_eng.city
			},
			get_mainpage_info() {
				this.$ajax({
					method: 'get',
					url: global_.IpUrl + '/house/price/' + this.city_name_en + '/mainpage_overview'
				}).then(function(resopnse) {
					if (resopnse.data.code == 0) {
						this.average_price = '' + (parseFloat(resopnse.data.data[0]) / 10000)
						
					} else {
						iView.Message.info(response.data.msg)
						this.average_price = '暂无该地区房价信息'
					}
				}.bind(this))
			},
		}
	}
</script>

<style scoped>
.body {
		height: 100%;
		width: 100%;
		padding: 0px;
		margin-top: 12px;
		display: block;
		position: relative;
		background-position-y: 0px
}	
.topic_line{
	width: 500px;
	height: 40px;
	margin-left: 50px;
	margin-top: 150px;
	z-index: 1;
	float: left;
	z-index: 10;
	position: absolute;
}
.swiper-container {
	width: 100%; 
	max-width: 1920px;
	min-width: 1024px;
	height: 700px;
	position: relative;
}
.swiper-wrapper {width: 100%; height: 100%; }
.swiper-slide { width: 100%;   height: 100%; z-index: 1;}
.swiper-pagination-bullet { 
	width:0.833rem;
    height: 0.833rem;
	display: inline-block;
	background: #7c5e53;
}  
.swiper-slide img{
	width: 100%;
	height: 100%;
	background-repeat: no-repeat;
	background-size: cover;
}

.background {
	width: 100%;
	max-width: 1920px;
	min-width: 1024px;
	height: 700px;
	background-image: url(../assets/main_bg.jpg);
	background-repeat: no-repeat;
	background-size: cover;
	padding-top: 1px;
}
.search_line{
	width: 500px;
	height: 40px;
	margin-left: 100px;
	margin-top: 300px;
	float: left;
	z-index: 10;
	position: absolute;
}
.search_block{
	width: 400px;
	height: 40px;
	opacity: 0.5;
	display: block;
	float: left;
}
.search_button{
	width: 80px;
	height: 40px;
	margin-left: 10px;
	background-color: darkred;
	opacity: 0.7;
	float: left;
	display: block;
	font-size: 16px;
	color: white;
	font-weight: 600;
	border: 0;
	border-radius: 5px;
}
.price {
	width: 250px;
	height: 250px;
	background-color: white;
	margin-top: 200px;
	margin-left: 70%;
	filter: alpha(Opacity=70);
	-moz-opacity: 0.7;
	opacity: 0.7;
	z-index: 10;
	position: absolute;
}
.city {
		width: 250px;
		height: 100px;
		margin-top: 20px;
		z-index: 2;
		font-family: "黑体";
	}	
.price_body{
	width: 250px;
	height: 60px;
}
	.erShouFang {
		width: 180px;
		height: 240px;
		background-color: white;
		border: 1px solid lightgray;
		z-index: 1;
		float: left;
		margin-left: 5%;

	}

	.erShouName {
		font-size: 16px;
		font-weight: 500;
		text-align: left;
	}

	.time {
		font-size: 13px;
		color: #999;
	}

	.bottom {
		margin-top: 13px;
		line-height: 12px;
	}



	.image {
		width: 100%;
		height: 120px;
		display: block;
	}

	.clearfix:before,
	.clearfix:after {
		display: table;
		content: "";
	}

	.clearfix:after {
		clear: both
	}
</style>
