<template>
	<div class="body">
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
						<el-checkbox v-model="underground" label="近地铁" border class="bar_2_2"></el-checkbox>
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
							<p class="bar_2_5" style="margin-top: 6px;color: white;">
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
							<el-button slot="reference" id="show_area" style="border: 0px;height: 33px;background-color: rgb(249, 249, 249);" @click="default_click">默认</el-button>
						</div>
						<div class="tip">
							<el-popover placement="bottom"  trigger="click" v-model='single_price_value'>
								<el-table :data="single_price_data" @row-click="show_single_price_select">
									<el-table-column width="150" property="single_price"></el-table-column>
								</el-table>
								<el-button slot="reference" id="show_single_price" style="border: 0px;height: 33px;width: 70px;background-color: rgb(249, 249, 249);">单价</el-button>
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
								<el-button slot="reference" id="show_total_price" style="border: 0px;height: 33px;width: 70px;background-color: rgb(249, 249, 249);">总价</el-button>
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
								<el-button slot="reference" id="show_total_area" style="border: 0px;height: 33px;width: 70px;background-color: rgb(249, 249, 249);">面积</el-button>
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
				<div class="list">
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import global_ from '@/components/Global'
	import store from '@/store'
	export default {
		data() {
			return {
				radio: '1',
				radio1: '1',
				radio2: '1',
				area_value: false,
				area: '选择面积',
				area_data: [{
						area: '不限',
					}, {
						area: '0～50平',
					},
					{
						area: '50～70平',
					}, {
						area: '70～90平',
					}, {
						area: '90～120平',
					}, {
						area: '120～150平',
					}, {
						area: '150～200平',
					}, {
						area: '200平以上',
					}
				],
				price_value: false,
				price: '选择价格',
				price_data: [{
					price: '不限',
				}, {
					price: '0～60w'
				}, {
					price: '60～100w'
				}, {
					price: '100～150w'
				}, {
					price: '150～200w'
				}, {
					price: '200～300w'
				}, {
					price: '300～500w'
				}, {
					price: '500w以上'
				}],
				house_value: false,
				house: "选择户型",
				house_data: [{
					house: '居室不限'
				}, {
					house: '一室'
				}, {
					house: '两室'
				}, {
					house: '三室'
				}, {
					house: '四室'
				}, {
					house: '五室'
				}, {
					house: '五室以上'
				}],
				region_value: false,
				region: "选择地区",
				region_data: [],
				
				underground: false,
				five_year:false,
				decoration:false,
				price_low:false,
				watch:false,
				south_north:false,
				
				single_price_value: false,
				single_price:'单价',
				single_price_data:[
					{
						single_price:'从高到低',
					},{
						single_price:"从低到高"
					}
				],
				total_price_value: false,
				total_price:'总价',
				total_price_data:[
					{
						total_price:'从高到低',
					},{
						total_price:"从低到高"
					}
				],
				total_area_value: false,
				total_area:'面积',
				total_area_data:[
					{
						total_area:'从高到低',
					},{
						total_area:"从低到高"
					}
				],
			};
		},
		mounted() {
			this.set_region()
		},
		methods: {
			set_region() {
				let temp_region = this.get_region
				for (var i = 0; i < temp_region.length; i++) {
					var temp = {}
					temp['region'] = temp_region[i]
					this.region_data.push(temp)
				}

			},
			show_area_select(row) {
				this.area = row.area
				this.area_value = false
			},
			show_price_select(row) {
				this.price = row.price
				this.price_value = false
			},
			show_house_select(row) {
				this.house = row.house
				this.house_value = false
			},
			show_region_select(row) {
				this.region = row.region
				this.region_value = false
			},
			show_single_price_select(row){
				this.single_price = row.single_price
				this.single_price_value =false
			},
			show_total_price_select(row){
				this.total_price = row.total_price
				this.total_price_value =false
			},
			show_total_area_select(row){
				this.total_area = row.total_area
				this.total_area_value =false
			},
			default_click(){
				
			},
			get_data(){
				var self = this
				self.$ajax({
					url:global_.IpUrl,
					methods:'post',
					data:{
						price_selcet: self.price,
						area_select: self.area,
						house_select:self.house,
						region_select: self.region,
						underground: self.underground,
						five_year:self.five_year,
						decoration:self.decoration,
						price_low:self.price_low,
						watch:self.watch,
						south_north:self.south_north,
					}
				})
			}
			
			
		},
		computed: {
			get_region() {
				var temp_region = this.get_city
				var arr = this.get_city.split('')
				if (arr[arr.length - 1] == "市") {
					arr.splice(arr.length - 1, 1)
					temp_region = arr.join('')
				}
				return global_.city_region_mapping[temp_region]
			},
			get_city() {
				return store.state.area.city
			}
		}
	}
</script>

<style scoped>
	.body {
		width: 100%;
		height: 1000px;
		min-width: 1273px;
	}

	.choose_body {
		width: 100%;
		height: 1000px;
		background-color: white;
		padding-left: 50%;
	}

	.Content {
		width: 950px;
		height: 950px;
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
		width: 70px;
		height: 25px;
		background-color: rgb(226, 226, 226);
		margin-top: 12px;
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
		height: 100px;
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
		height: 530px;
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
</style>
