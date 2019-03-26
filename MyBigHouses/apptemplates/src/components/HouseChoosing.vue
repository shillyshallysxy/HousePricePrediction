<template>
	<div class="body"  v-loading.fullscreen.lock="fullscreenLoading">
		<div class="choose_body">
			<div class="Content">
				<div class="bar">
					<div class="bar_1">
						<el-popover placement="bottom" width="200" trigger="click" v-model='price_value'>
							<el-table :data="price_data" @row-click="show_price_select">
								<el-table-column width="150" property="price"></el-table-column>
							</el-table>
							<el-button slot="reference" id="show_area" class="bar_1_1">{{price}}</el-button>
						</el-popover>
					</div>
					<div class="bar_1">
						<!-- <div class="bar_1_1" id="show_area">
							<p style="margin-top: 32px;">面积：90-120平</p>
						</div> -->
						<el-popover placement="bottom" width="200" trigger="click" v-model='area_value'>
							<el-table :data="area_data" @row-click="show_area_select">
								<el-table-column width="150" property="area"></el-table-column>
							</el-table>
							<el-button slot="reference" id="show_area" class="bar_1_1">{{area}}</el-button>
						</el-popover>
					</div>
					<div class="bar_1">
						<el-popover placement="bottom" width="200" trigger="click" v-model='house_value'>
							<el-table :data="house_data" @row-click="show_house_select">
								<el-table-column width="150" property="house"></el-table-column>
							</el-table>
							<el-button slot="reference" id="show_area" class="bar_1_1">{{house}}</el-button>
						</el-popover>
					</div>
					<div class="bar_1">
						<el-popover placement="bottom" width="200" trigger="click" v-model='region_value'>
							<el-table :data="region_data" @row-click="show_region_select">
								<el-table-column width="150" property="region"></el-table-column>
							</el-table>
							<el-button slot="reference" id="show_area" class="bar_1_1">{{region}}</el-button>
						</el-popover>
					</div>
					<div class="bar_2">

						<p class="bar_2_1">标签：</p>
						<el-checkbox v-model="underground" label="近地铁" border class="bar_2_2" style=""></el-checkbox>
						<el-checkbox v-model="five_year" label="满五年" border class="bar_2_2"></el-checkbox>
						<el-checkbox v-model="decoration" label="精装修" border class="bar_2_2"></el-checkbox>
						<el-checkbox v-model="price_low" label="总价低" border class="bar_2_2"></el-checkbox>
						<el-checkbox v-model="watch" label="随时看" border class="bar_2_2"></el-checkbox>
						<el-checkbox v-model="south_north" label="南北向" border class="bar_2_2"></el-checkbox>
						<!-- <div class="bar_2_2">
							<p class="bar_2_5">近地铁</p>
						</div>
						<div class="bar_2_2">
							<p class="bar_2_5">满五年</p>
						</div>
						<div class="bar_2_2">
							<p class="bar_2_5">满两年</p>
						</div>
						<div class="bar_2_2">
							<p class="bar_2_5">精装修</p>
						</div>
						<div class="bar_2_2">
							<p class="bar_2_5">总价低</p>
						</div>
						<div class="bar_2_2">
							<p class="bar_2_5">随时看</p>
						</div>
						<div class="bar_2_3">
							<p class="bar_2_5">南北向</p>
						</div>
						<el-checkbox v-model="checked3" label="备选项1" border class="bar_2_2"></el-checkbox>
						<el-checkbox v-model="checked4" label="备选项2" border class="bar_2_2"></el-checkbox> -->
						<div class="bar_2_4">
							<p class="bar_2_5" style="margin-top: 6px;color: white;cursor: pointer;" @click="get_select_List_first">
								筛选
							</p>
						</div>
					</div>
				</div>
				<div class="middle">
					<div class="middle1"></div>
					<p class="middle2">查询结果</p>
				</div>
				<div class="tips">
					<div>
						<div class="tip">
							<el-button slot="reference" id="show_area" style="border: 0px;height: 33px;background-color: rgb(249, 249, 249);" @click="default_click" index='0'>默认</el-button>
						</div>
						<div class="tip">
							<el-popover placement="bottom"  trigger="click" v-model='single_price_value'>
								<el-table :data="single_price_data" @row-click="show_single_price_select">
									<el-table-column width="150" property="single_price"></el-table-column>
								</el-table>
								<el-button slot="reference" id="show_single_price" style="border: 0px;height: 33px;width: 70px;background-color: rgb(249, 249, 249);" index='1'>单价</el-button>
							</el-popover>
							<div class="tip2">
								<i class="el-icon-caret-top"></i>
							</div>
							<div class="tip2" style="margin-top: -20px;">
								<i class="el-icon-caret-bottom"></i>
							</div>
						</div>
						
						<div class="tip">
							<el-popover placement="bottom"  trigger="click" v-model='total_price_value'>
								<el-table :data="total_price_data" @row-click="show_total_price_select">
									<el-table-column width="150" property="total_price"></el-table-column>
								</el-table>
								<el-button slot="reference" id="show_total_price" style="border: 0px;height: 33px;width: 70px;background-color: rgb(249, 249, 249);" index='2'>总价</el-button>
							</el-popover>
							<div class="tip2">
								<i class="el-icon-caret-top"></i>
							</div>
							<div class="tip2" style="margin-top: -20px;">
								<i class="el-icon-caret-bottom"></i>
							</div>
						</div>
						<div class="tip">
							<el-popover placement="bottom"  trigger="click" v-model='total_area_value'>
								<el-table :data="total_area_data" @row-click="show_total_area_select">
									<el-table-column width="150" property="total_area"></el-table-column>
								</el-table>
								<el-button slot="reference" id="show_total_area" style="border: 0px;height: 33px;width: 70px;background-color: rgb(249, 249, 249);" index='3'>面积</el-button>
							</el-popover>
							<div class="tip2">
								<i class="el-icon-caret-top"></i>
							</div>
							<div class="tip2" style="margin-top: -20px;">
								<i class="el-icon-caret-bottom"></i>
							</div>
						</div>
					</div>
				</div>
				<div class="list_content">
					<ul class="list">
						<p v-if="isnull">
							没有该条件下的筛选结果
						</p>
						<li class="collect" v-for="(o, index) in favor_info" key='o.id'>
							<img :src="o.img_url" class="item_img" />
					
							<div class="block">
								<p style="font-size: 18px;font-weight: 500;cursor: pointer;" @click="go_to_detail(o.id,index)">
									{{o.description}}
								</p>
								<p class="desCollect">
									{{o.layout}}，{{o.area}}平米，{{o.layer}}
									{{o.garden}}，{{o.architecture}}，{{o.built_year}}
									{{o.developer}}
								</p>
								
					
							</div>
							<div class="item_right">
								<p class="textColor">
									{{o.total_price}}万
								</p>
								<p style="font-size: 12px;font-weight: 300;">
									单价：{{o.price}} 元/平米
								</p>
								<p style="font-size: 12px;font-weight: 300;margin-top: 20px;">
									{{o.star_count}}人已收藏
								</p>
							</div>
							<div class="line1"></div>
						</li>
					</ul>
					<v-pagination v-if="hackReset" :total="total" :currentPage='current' @pagechange="pagechange" :display = 'display'></v-pagination>	
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import global_ from '@/components/Global'
	import store from '@/store'
	import {
		getCookie,
		setCookie,
		delCookie
	} from '@/utils/utils'
	import pagination from '@/components/MyPagenation'
	export default {
		//引入分页模块
		components: {
			'v-pagination': pagination,
		},
		data() {
			return {
				isnull: false,  //表示搜索结果是否为空
				hackReset : true, //刷新分页
				sort_index : 0, //排序的种类参数
				favor_info: [], //搜索信息的list
				//分页实现内容
				total: 0, // 记录总条数
				display: 14, // 每页显示条数
				current: 1, // 当前的页数
				istrue: false, 
				area_value: false,//面积是否选择
				area: '选择面积',//面积选项框中的内容
				area_paras : '0~0',//面积向后台传参格式
				// 面积选项下拉框内容
				area_data: [{
						area: '不限',
						area_para: '0~0',
					}, {
						area: '0～50平',
						area_para: '0~50',
					},
					{
						area: '50～70平',
						area_para: '50~70',
					}, {
						area: '70～90平',
						area_para: '70~90',
					}, {
						area: '90～120平',
						area_para: '90~120',
					}, {
						area: '120～150平',
						area_para: '120~150',
					}, {
						area: '150～200平',
						area_para: '150~200',
					}, {
						area: '200平以上',
						area_para: '200~200',
					}
				],
				price_value: false,//价格是否选择
				price: '选择价格',//价格选项框中内容
				price_paras:'0~0',//价格向后台传参格式
				// 价格下拉框内容
				price_data: [{
					price: '不限',
					price_para:'0~0',
				}, {
					price: '0～60w',
					price_para:'0~60',
				}, {
					price: '60～100w',
					price_para:'60~100',
				}, {
					price: '100～150w',
					price_para:'100~150',
				}, {
					price: '150～200w',
					price_para:'150~200',
				}, {
					price: '200～300w',
					price_para:'200~300',
				}, {
					price: '300～500w',
					price_para:'300~200',
				}, {
					price: '500w以上',
					price_para:'500~500',
				}],
				house_value: false, //户型是否选择
				house: "选择户型", //户型选项框中的内容
				house_paras:'0', //户型像后台传参格式
				//户型下拉框内容
				house_data: [{
					house: '居室不限',
					house_para: '0'
				}, {
					house: '一室',
					house_para: '1'
				}, {
					house: '两室',
					house_para: '2'
				}, {
					house: '三室',
					house_para: '3'
				}, {
					house: '四室',
					house_para: '4'
				}, {
					house: '五室',
					house_para: '5'
				}, {
					house: '五室以上',
					house_para: '6'
				}],
				region_value: false, // 区域是否选择
				region: "选择地区", //区域选项框中的内容
				region_data: [],//区域下拉框内容
				
				underground: false,  //地铁是否勾选
				five_year:false,//满五年是否勾选
				decoration:false, //精装修是否勾选
				price_low:false, //价格低是否勾选
				watch:false,	// 随时看是否勾选
				south_north:false, //南北向收否勾选
				
				single_price_value: false, //单价排序是否勾选
				single_price:'单价',  //单价选项卡中的显示内容
				// 单价排序的可选内容
				single_price_data:[
					{
						single_price:'从高到低',
						single_price_index :1,
					},{
						single_price:"从低到高",
						single_price_index :2,
					}
				],
				total_price_value: false,//总价排序是否勾选
				total_price:'总价', //总价选项卡中的显示内容
				//总价排序的可选内容
				total_price_data:[
					{
						total_price:'从高到低',
						total_price_index:3,
					},{
						total_price:"从低到高",
						total_price_index:4,
					}
				],
				total_area_value: false,//面积排序是否勾选
				total_area:'面积',// 面积选项卡中的显示内容
				//面积排序的可选内容
				total_area_data:[
					{
						total_area:'从高到低',
						total_area_index:5,
					},{
						total_area:"从低到高",
						total_area_index:6,
					}
				],
			};
		},
		//mounted 钩子
		mounted() {
			// 获取城市区域信息
			this.set_region()
			// 获取初始话页面信息
			this.get_select_List()
			
		},
		methods: {
			//进入房价信息详情页
			go_to_detail(id) {
				this.$router.push({
					path: 'ItemPage',
					query: {
						HouseId: id
					}
				})
			},
			// 获取搜索信息的第一页
			get_select_List_first(){
				this.current=1 //当前页码重置为1
				this.hackReset = false
				this.$nextTick(()=>{
					this.hackReset=true
				})
				
				this.get_select_List()
			},
			get_select_List(){
				//加载动画
				const loading = this.$loading({
					lock: true,
					text: 'Loading',
					spinner: 'el-icon-loading',
					background: 'rgba(255,255,255,0.8)'
				});
				var data = {}
				this.istrue = true
				data["area"] = this.area_paras,//获取面积
				data["price"] = this.price_paras//获取价格
				data["house"] = this.house_paras,//获取居室
				data["region"] = this.region=="选择地区"?"":this.region,//获取地区
				data["underground"] = this.underground?1:0//获取地铁
				data["five_year"] = this.five_year?1:0//获取是否满五年
				data["decoration"] = this.decoration?1:0//获取是否精装修
				data["price_low"] = this.price_low?1:0//获取是否低价格
				data["watch"] = this.watch?1:0//获取是否随时能看
				data["south_north"] = this.south_north?1:0//获取是否南北向
				data["city"] = this.get_city//获取城市
				data["page"] = this.current//获取当前页码
				data["sort"] = this.sort_index//获取排序方式
				var arr = getCookie('csrftoken')//获取csrktoken
				var _this = this
				_this.$ajax({
					url:global_.IpUrl+ "/house/filter",
					method:"post",
					data:data,
					headers: {
						'Content-Type': 'application/x-www-form-urlencoded',
						'X-CSRFToken': arr
					}
				}).then(function(response){
					if(response.data.code != 0)
					{
						loading.close();
					}
					else
					{
						if(response.data.total_item_num == 0)
						{
							//如果返回个数为0，则显示无数据
							_this.isnull = true
							_this.favor_info = []
							_this.total = response.data.total_item_num
						}
						else{
							_this.isnull = false
							var favor = response.data.data
							_this.favor_info = []
							//获取返回的数据，并加载到页面
							for (var i = 0; i < favor.length; i++) {
								var temp = {}
								temp["description"] = favor[i].description
								temp["layout"] = favor[i].layout
								temp["layer"] = favor[i].layer
								temp["built_year"] = favor[i].built_year
								temp["area"] = favor[i].area
								temp["price"] = favor[i].price
								temp["total_price"] = favor[i].total_price
								temp["orientation"] = favor[i].orientation
								temp["garden"] = favor[i].garden
								temp["developer"] = favor[i].developer
								temp["architecture"] = favor[i].architecture
								temp["id"] = favor[i].id
								temp["img_url"] = favor[i].img_url
								temp["star_count"] = favor[i].star_count
								_this.favor_info.push(temp)
								_this.total = response.data.total_item_num
							
							}						
						}
						loading.close();
						
					}
				})
			},
// 			get_select_page_change(){
// 				
// 				console.log("get")
// 				var _this = this 
// 				_this.$ajax({
// 					url: global_.IpUrl+"/house/filter?page="+this.current,
// 					method:'get'
// 				}).then(function(response){
// 					if(response.data.code != 0)
// 					{
// 						console.log(response.data.msg)
// 					}
// 					else
// 					{
// 						var favor = response.data.data
// 						_this.favor_info = []
// 						for (var i = 0; i < favor.length; i++) {
// 							var temp = {}
// 							temp["description"] = favor[i].description
// 							temp["layout"] = favor[i].layout
// 							temp["layer"] = favor[i].layer
// 							temp["built_year"] = favor[i].built_year
// 							temp["area"] = favor[i].area
// 							temp["price"] = favor[i].price
// 							temp["total_price"] = favor[i].total_price
// 							temp["orientation"] = favor[i].orientation
// 							temp["garden"] = favor[i].garden
// 							temp["developer"] = favor[i].developer
// 							temp["architecture"] = favor[i].architecture
// 							temp["id"] = favor[i].id
// 							temp["img_url"] = favor[i].img_url
// 							temp["star_count"] = favor[i].star_count
// 							_this.favor_info.push(temp)
// 							_this.total = response.data.total_item_num
// 							
// 						}
// 					}
// 				})
// 			},
			//分页改变事件，向后台请求具体页码的信息
			pagechange(page) {
				this.current = page
				this.get_select_List()
				document.documentElement.scrollTop=0
				
				
			},
// 			get_default_list() {
// 				const loading = this.$loading({
// 					lock: true,
// 					text: 'Loading',
// 					spinner: 'el-icon-loading',
// 					background: 'rgba(0, 0, 0, 0.7)'
// 				});
// 				
// 				let url = global_.IpUrl + '/house/list/'+this.get_city_eng+'?page_num=' + this.current
// 				this.$ajax({
// 					url: url,
// 					method: 'get',
// 				}).then(function(response) {
// 					if (response.data.code === 0) {
// 						var favor = response.data.data
// 						
// 						this.favor_info = []
// 						for (var i = 0; i < favor.length; i++) {
// 							var temp = {}
// 							temp["description"] = favor[i].description
// 							temp["layout"] = favor[i].layout
// 							temp["layer"] = favor[i].layer
// 							temp["built_year"] = favor[i].built_year
// 							temp["area"] = favor[i].area
// 							temp["price"] = favor[i].price
// 							temp["total_price"] = favor[i].total_price
// 							temp["orientation"] = favor[i].orientation
// 							temp["garden"] = favor[i].garden
// 							temp["developer"] = favor[i].developer
// 							temp["architecture"] = favor[i].architecture
// 							temp["id"] = favor[i].id
// 							temp["img_url"] = favor[i].img_url
// 							temp["star_count"] = favor[i].star_count
// 							this.favor_info.push(temp)
// 							this.total = response.data.total_item_num
// 							
// 						}
// 						console.log(this.total)
// 						loading.close();
// 					} else {
// 						loading.close();
// 						iView.Message.info(response.data.msg)
// 					}
// 				}.bind(this))
// 			
// 			},
			//获取当前城市的区信息，并显示在区域选择框中
			set_region() {
				
				let temp_region = this.get_region
				for (var i = 0; i < temp_region.length; i++) {
					var temp = {}
					temp['region'] = temp_region[i]
					this.region_data.push(temp)
				}

			},
			show_area_select(row) {
				this.area = row.area //获取选项信息
				this.area_paras = row.area_para //修改向后台的传参
				this.area_value = false //隐藏选项框
			},
			//同上
			show_price_select(row) {
				this.price = row.price
				this.price_paras = row.price_para
				this.price_value = false
				
			},
			//同上
			show_house_select(row) {
				this.house = row.house
				this.house_paras = row.house_para
				this.house_value = false
			},
			
			show_region_select(row) {
				this.region = row.region
				this.region_value = false
				this.get_select_List_first() //请求第一页信息
			},
			//同上
			show_single_price_select(row){
				this.sort_index = row.single_price_index
				this.single_price_value =false
				this.get_select_List_first()
			},
			//同上
			show_total_price_select(row){
				this.sort_index = row.total_price_index
				this.total_price_value =false
				this.get_select_List_first()
			},
			//同上
			show_total_area_select(row){
				this.sort_index = row.total_area_index
				this.total_area_value =false
				this.get_select_List_first()
			},
			default_click(){
				
			},
// 			get_data(){
// 				var self = this
// 				self.$ajax({
// 					url:global_.IpUrl,
// 					methods:'post',
// 					data:{
// 						price_selcet: self.price,
// 						area_select: self.area,
// 						house_select:self.house,
// 						region_select: self.region,
// 						underground: self.underground,
// 						five_year:self.five_year,
// 						decoration:self.decoration,
// 						price_low:self.price_low,
// 						watch:self.watch,
// 						south_north:self.south_north,
// 					}
// 				})
// 			}
			
			
		},
		computed: {
			//获取区域信息
			get_region() {
				var temp_region = this.get_city
				var arr = this.get_city.split('')
				if (arr[arr.length - 1] == "市") {
					arr.splice(arr.length - 1, 1)
					temp_region = arr.join('')
				}
				return global_.city_region_mapping[temp_region]
			},
			//获取城市信息
			get_city() {
				return store.state.area.city
			},
			//获取城市拼音
			get_city_eng(){
				return store.state.area_eng.city
			}
		}
	}
</script>

<style scoped>
	.body {
		width: 100%;
		height: 100%;
		min-width: 1050px;
	}

	.choose_body {
		width: 100%;
		height: 3000px;
		background-color: white;
		padding-left: 50%;
	}

	.Content {
		width: 950px;
		height: 3000px;
		margin-left: -475px;
		padding-top: 50px;
	}

	.bar {
		width: 100%;
		height: 220px;
		border: 1px solid rgb(237, 237, 237);
		border-top: 5px solid #009688;
		background-color: white;
	}

	.bar_1 {
		width: 200px;
		height: 100px;
		margin-left: 30px;
		margin-top: 30px;
		float: left;
		border-radius: 20px;
	}

	.bar_1_1 {
		width: 200px;
		height: 100px;
		border: 1px solid rgb(224, 224, 224);
		background-color: rgb(249, 249, 249);
		border-radius: 20px;
		font-size: 20px;
	}

	.bar_1_2 {
		width: 400px;
		height: 200px;
		z-index: 10;
		border: 1px solid black;
		border-radius: 20px;
		background-color: white;
		margin-top: 10px;
		padding-top: 20px;
		display: none;
		position: absolute;
		z-index: 10;
	}

	.line {
		height: 1px;
		width: 80%;
		background: black;
		overflow: hidden;
		margin-left: 10%;
	}

	.menu_price {
		width: 320px;
		margin-left: 40px;
		height: 90px;
		margin-top: 10px;
	}

	.price_radio {
		width: 100px;
		height: 30px;
		text-align: left;
		font-size: 12px;
		float: left;
	}

	.zdy_price {
		width: 320px;
		margin-left: 40px;
		height: 40px;
		margin-top: 15px;
		float: left;
	}

	.zdy_text {
		font-size: 16px;
		float: left;
	}

	.zdy_input {
		width: 80px;
		height: 30px;
		border-radius: 5px;
		float: left;
	}

	.zdy_button {
		width: 40px;
		height: 25px;
		border-radius: 5px;
		font-size: 12px;
		color: white;
		background-color: #009688;
	}

	.bar_2 {
		width: 100%;
		height: 50px;
		margin-top: 150px;
	}

	.bar_2_1 {
		float: left;
		font-family: "黑体";
		font-size: 20px;
		font-weight: 400;
		margin-top: 10px;
		margin-left: 30px;
	}

	.bar_2_2 {
		/*未选中*/
		width: 80px;
		background-color: rgb(226, 226, 226);
		margin-top: 12px;
		margin-left: 0px;
		float: left;
		border-radius: 5px;
		padding: 1px;
	}

	.bar_2_3 {
		/*已选中*/
		width: 60px;
		height: 25px;
		background-color: rgb(200, 200, 200);
		margin-left: 10px;
		margin-top: 12px;
		float: left;
		border-radius: 5px;
		padding: 1px;
	}

	.bar_2_4 {
		/*筛选按钮*/
		width: 80px;
		height: 35px;
		background-color: #009688;
		float: right;
		border-radius: 5px;
		margin-right: 50px;
		font-weight: 500;
		font-size: 10px;
		margin-top: 6px;
		padding: 1px;
		padding-top: 2px;
	}

	.bar_2_5 {
		font-size: 10px;
		font-weight: 500;
		margin-top: 3px;
	}

	.middle {
		width: 100%;
		height: 100px;
		border: 0px;
		padding-top: 1px;
	}

	.middle1 {
		width: 20px;
		height: 50px;
		border: 0px;
		background-color: rgb(154, 154, 154);
		margin-top: 30px;
		float: left;
	}

	.middle2 {
		font-size: 24px;
		float: left;
		margin-top: 40px;
		margin-left: 20px;
	}

	.tips {
		width: 100%;
		height: 60px;
		border: 0px;
	}

	.tip {
		width: 100px;
		height: 40px;
		background-color: white;
		border: 1px solid rgb(224, 224, 224);
		background-color: rgb(249, 249, 249);
		border-top: 5px solid #009688;
		float: left;
	}

	.tip_1 {
		font-size: 15px;
		margin-top: 6px;
		float: left;
		margin-left: 20px;
	}

	.tip2 {
		float: right;
		width: 20px;
		height: 10px;
		margin-top: 4px;
		margin-right: 8px;
	}

	.list {
		width: 100%;
		height: 2400px;
		border: 0px;
	}

	.el-dropdown-link {
		cursor: pointer;
		color: #409EFF;
	}

	.el-icon-arrow-down {
		font-size: 12px;
	}

	.demonstration {
		display: block;
		color: #8492a6;
		font-size: 14px;
		margin-bottom: 20px;
	}
	
	.list {
		width: 100%;
		position: relative;
		overflow: hidden;
	}
	
	.block {
		width: 500px;
		height: 150px;
		display: inline-block;
		padding: 0;
		position: absolute;
		top: 0px;
		left: 210px;
	}
	
	.item_img {
		max-height: 145px;
		max-width: 200px;
		min-height: 145px;
		min-width: 200px;
		background-size: 100% 100%;
		display: inline-block;
		float: left;
	}
	
	.desCollect {
		font-size: 12px;
		font-weight: 300;
		margin-left: 10px;
		margin-top: 20px;
		height: 80px;
		width: 400px;
	}
	
	.item_right {
		height: 150px;
		width: 150px;
		display: inline-block;
		padding: 0;
		position: absolute;
		top: 0px;
		left: 800px;
	}
	.textColor {
		font-size: 28px;
		font-weight: 400;
		margin-top: 10px;
		color: rgb(252, 124, 0);
	}
	.collect {
		min-height: 150px;
		width: 950px;
		max-height: 150px;
		float: left;
		text-align: left;
		padding-top: 0;
		position: relative;
		margin-top: 20px;
		list-style: none;
	}
	.list_content {
		width: 950px;
		height: 2400px;
		padding-top: 30px;
	}
</style>
