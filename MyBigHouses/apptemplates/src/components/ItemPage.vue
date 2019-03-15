<template>
	<div style="background-color: white;min-height: 700px;width: 100%;background: white;padding-top: 1px;">
		<div style="margin: 0;padding: 0;background-color: rgb(237,237,237);min-width: 1200px;max-width: 100%;height: 200px;padding-top: 1px;">
			<div style="min-width: 500px;max-width: 500px;max-height: 60%;min-height: 60%;margin-top: 60px;margin-left: 10%;display: inline-block;float: left;">
				<p style="font-size: 28px;text-align: left;">
					{{Detail_info.description}}
				</p>
			</div>
			<div style="min-width: 80px;max-width: 80px;min-height: 40px;max-height: 40px;display: inline-block;float: left;margin-top: 80px;margin-left: 80px;">
				<p style="font-size: 24px;color: gray;">
					发售中
				</p>
			</div>
			<div style="background-color: white;min-width: 120px;max-width: 120px;min-height: 40px;max-height: 40px;display: inline-block;float: left;margin-top: 50px;margin-left: 160px;border: 1px solid black;">
				<div style="min-width: 38px;max-width: 38px;min-height: 38px;max-height: 38px;display: inline-block;float: left;border-right: 1px solid black;">
					<i class="el-icon-view" style="font-size: 20px;margin-top: 10px;"></i>
				</div>
				<div style="min-width: 78px;max-width: 78px;min-height: 38px;max-height: 38px;display: inline-block;float: left;">
					<p style="font-size: 16px;margin-top: 8px;font-family: arial;">
						{{Detail_info.view_count}}
					</p>
				</div>
			</div>
			<div style="background-color: white;min-width: 120px;max-width: 120px;min-height: 40px;max-height: 40px;display: inline-block;float: left;margin-top: 50px;margin-left: 20px;border: 1px solid black;">
				<div style="min-width: 38px;max-width: 38px;min-height: 38px;max-height: 38px;display: inline-block;float: left;border-right: 1px solid black;" v-if="!Detail_info.star_flag">
					<i class="el-icon-star-off" style="font-size: 20px;margin-top: 10px;" @click="star()" ></i>
				</div>
				<div style="min-width: 38px;max-width: 38px;min-height: 38px;max-height: 38px;display: inline-block;float: left;border-right: 1px solid black;" v-else>
					<i class="el-icon-star-on" style="font-size: 20px;margin-top: 10px;" @click="unstar()" ></i>
				</div>
				<div style="min-width: 78px;max-width: 78px;min-height: 38px;max-height: 38px;display: inline-block;float: left;">
					<p style="font-size: 16px;margin-top: 8px;font-family: arial;">
						{{Detail_info.star_count}}
					</p>
				</div>
			</div>
		</div>
		
		<div style="max-width: 100%;min-width: 1200px;height: 500px;padding-top: 1px;">
			<div style="background-color: white;max-width: 70%;min-width: 950px;height: 80%;margin-left: 15%;margin-top: 30px;">
				<div style="min-width: 400px;max-width: 400px;min-height: 400px;max-height: 400px;display: inline-block;float: left;">
					<img src="../assets/2.jpg" style="min-width: 400px;max-width: 400px;min-height: 300px;max-height: 300px;background-size: 100% 100%;" />
					<div style="display: block;position: relative;margin-top: 8px;width: 400px;height: 82px;">
						<div v-bind:class="{pre: true}"> < </div>
						<ul v-bind:class="{img_ul: true}">
							<li v-bind:class="{img_li: true}">
								<img src="../assets/2.jpg" style="min-width: 144px;max-width: 144px;min-height: 82px;max-height: 82px;background-size: 100% 100%;" />
							</li>
							<li v-bind:class="{img_li: true}">
								<img src="../assets/2.jpg" style="min-width: 144px;max-width: 144px;min-height: 82px;max-height: 82px;background-size: 100% 100%;" />
							</li>
						</ul>
						<div v-bind:class="{next: true}"> > </div>
					</div>
				</div>
				<div style="min-width: 500px;max-width: 500px;min-height: 400px;max-height: 400px;display: inline-block;float: left;margin-left: 20px;">
					<div style="min-width: 500px;max-width: 500px;min-height: 100px;max-height: 100px;">
						<p style="font-size: 64px;color: red;float: left;margin-left: 40px;font-family: arial;">{{Detail_info.total_price}}</p>
						<p style="font-size: 24px;color: black;float: left;margin-top: 40px;margin-left: 10px;">万</p>
						<p style="font-size: 18px;color: black;float: right;margin-top: 50px;margin-right: 60px;">{{Detail_info.price}}元/平方</p>
					</div>
					<div style="margin-left: 50px;height: 2px;min-width: 400px;max-width: 400px;background:rgb(173,173,173);overflow:hidden;"></div>
					<div style="min-width: 500px;max-width: 500px;min-height: 100px;max-height: 100px;">
						<div style="min-width: 500px;max-width: 500px;min-height: 60px;max-height: 60px;">
							<p style="font-size: 28px;color: black;float: left;font-weight: 200;font-family: arial;font-weight: 400;margin-top: 10px;margin-left: 60px;">{{Detail_info.layout}}</p>
							<p style="font-size: 28px;color: black;float: left;font-weight: 200;font-family: arial;font-weight: 400;margin-top: 10px;margin-left: 60px;">{{Detail_info.orientation}}</p>
							<p style="font-size: 28px;color: black;float: left;font-weight: 200;font-family: arial;font-weight: 400;margin-top: 10px;margin-left: 60px;">{{Detail_info.area}}平米</p>
						</div>
						<div style="min-width: 500px;max-width: 500px;min-height: 40px;max-height: 40px;">
							<p style="font-size: 16px;color: black;float: left;font-weight: 100;font-family: arial;font-weight: 400;margin-top: 10px;margin-left: 50px;">{{Detail_info.layer}}</p>
							<p style="font-size: 16px;color: black;float: left;font-weight: 100;font-family: arial;font-weight: 400;margin-top: 10px;margin-left: 50px;">{{Detail_info.architecture}}</p>
							<p style="font-size: 16px;color: black;float: left;font-weight: 100;font-family: arial;font-weight: 400;margin-top: 10px;margin-left: 50px;">{{Detail_info.built_year}}年建</p>
						</div>
					</div>
					<div style="margin-left: 50px;height: 2px;min-width: 400px;max-width: 400px;background:rgb(173,173,173);overflow:hidden;"></div>
					<div style="min-width: 500px;max-width: 500px;min-height: 200px;max-height: 200px;">
						<div v-bind:class="{itemInfo: true}">
							<p style="font-family: 黑体;font-size: 16px;margin-top: 5px;display: inline-block;float: left;margin-left: 60px;">小区名称:</p>
							<p style="font-family: 黑体;font-size: 16px;margin-top: 5px;display: inline-block;float: left;margin-left: 150px;">{{Detail_info.garden}}</p>
						</div>
						<div v-bind:class="{itemInfo: true}">
							<p style="font-family: 黑体;font-size: 16px;margin-top: 5px;display: inline-block;float: left;margin-left: 60px;">所在地区:</p>
							<p style="font-family: 黑体;font-size: 16px;margin-top: 5px;display: inline-block;float: left;margin-left: 150px;">{{Detail_info.location}}</p>
						</div>
						<div v-bind:class="{itemInfo: true}">
							<p style="font-family: 黑体;font-size: 16px;margin-top: 5px;display: inline-block;float: left;margin-left: 60px;">开发公司:</p>
							<p style="font-family: 黑体;font-size: 16px;margin-top: 5px;display: inline-block;float: left;margin-left: 80px;">{{Detail_info.developer}}</p>
						</div>
						<div v-bind:class="{itemInfo: true}">
							<p style="font-family: 黑体;font-size: 16px;margin-top: 5px;display: inline-block;float: left;margin-left: 60px;">物业公司:</p>
							<p style="font-family: 黑体;font-size: 16px;margin-top: 5px;display: inline-block;float: left;margin-left: 80px;">{{Detail_info.property_company}}</p>
						</div>
						<div v-bind:class="{itemInfo: true}">
							<p style="font-family: 黑体;font-size: 16px;margin-top: 5px;display: inline-block;float: left;margin-left: 60px;">联系方式:</p>
							<p style="font-family: 黑体;font-size: 16px;margin-top: 5px;display: inline-block;float: left;margin-left: 135px;">{{Detail_info.contact}}</p>
						</div>
					</div>
				</div>
			</div>
		
			
		</div>
		
		<div style="margin-left: 180px;height: 1px;width: 70%;min-width: 700px;background:black;overflow:hidden;margin-top: 40px;"></div>
	</div>
</template>

<script>
	import store from '@/store'
	import global_ from '@/components/Global'
	import iView from 'iview'
	export default{
		data(){
			return{
				Detail_info:{
					description:'',
					view_count:'',
					star_count:'',
					total_price:'',
					price:'',
					layout:'',
					orientation:'',
					area:'',
					layer:'',
					architecture:'',
					built_year:'',
					garden:'',
					location:'',
					developer:'',
					property_company:'',
					contact:'',
					star_flag: ''
				}
			}
		},
		created(){
			var House_id = this.$route.query.HouseId
			var _this = this
			_this.$ajax({
				method: 'get',
				url: global_.IpUrl + '/house/detail/' + House_id,
			}).then(function(response){
				if(response.data.code===0){
					var house = response.data.data
					_this.Detail_info.description = house['description']
					_this.Detail_info.view_count = response.data.view_count
					_this.Detail_info.star_count = response.data.star_count
					_this.Detail_info.total_price = house['total_price']
					_this.Detail_info.price = house['price']
					_this.Detail_info.layout = house['layout']
					_this.Detail_info.orientation = house['orientation']
					_this.Detail_info.area = house['area']
					_this.Detail_info.layer = house['layer']
					_this.Detail_info.architecture = house['architecture']
					_this.Detail_info.built_year = house['built_year']
					_this.Detail_info.garden = house['garden']
					_this.Detail_info.location = house['location']
					_this.Detail_info.developer = house['developer']
					_this.Detail_info.property_company = house['property_company']
					_this.Detail_info.contact = house['contact']
					_this.Detail_info.star_flag = response.data.star_flag
				}else{
					
				}
			})
		},
		mounted() {
			
		},
		methods:{
			star(){
				var _this = this
				_this.$ajax({
					method: 'get',
					url: global_.IpUrl+"/user/star?house_id="+this.$route.query.HouseId
				}).then(function(response){
					if(response.data.code===0){
						_this.Detail_info.star_flag = response.data.star_flag
						_this.Detail_info.star_count = response.data.star_count
					}else{
						if(response.data.code ===3){
							iView.Message.info("请先登录")
							setTimeout(_this.go, 1000);
						}
					}
				})
			},
			unstar(){
				var _this = this
				_this.$ajax({
					method: 'get',
					url: global_.IpUrl+"/user/star?house_id="+this.$route.query.HouseId
				}).then(function(response){
					if(response.data.code===0){
						_this.Detail_info.star_flag = response.data.star_flag
						_this.Detail_info.star_count = response.data.star_count
					}else{
						if(response.data.code ===2){
							iView.Message.info("请先登录")
							setTimeout(this.go, 1000);
						}
					}
				})
			},
			go() {
				this.$router.push({path: "/login"})
			},
		}
	}
</script>

<style scoped>
.pre{
	position: absolute;
    top: 0;
    line-height: 82px;
    width: 30px;
    text-align: center;
    font-size: 20px;
    color: #cac9c9;
    opacity: .8;
    filter: alpha(opacity=80);
    background-color: #000;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
}
.next{
	position: absolute;
    top: 0;
    line-height: 82px;
    width: 30px;
    text-align: center;
    font-size: 20px;
    color: #cac9c9;
    opacity: .8;
    filter: alpha(opacity=80);
    background-color: #000;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
	right: 0;
}
.img_ul{
	white-space: nowrap;
    overflow: hidden;
    height: 82px;
    font-size: 0;
    margin-left: -75px;
    width: 530px;
}
.img_li {
    display: inline-block;
    width: 144px;
    height: 82px;
    margin-left: 20px;
    text-align: center;
}
.itemInfo{
	max-height: 40px;
	min-height: 40px;
	max-width: 500px;
	min-width: 500px;
	padding-top: 1px;
}
</style>
