<template>
	<div class="body">
		<div class="choose_body">
			<div class="Content">
				<div class="bar">
					<div class="bar_1">
						<el-col :span="12">
							<span class="demonstration">总价:</span>
							<el-dropdown trigger="click">
								<span class="el-dropdown-link">
									选择价格<i class="el-icon-arrow-down el-icon--right"></i>
								</span>
								<el-dropdown-menu slot="dropdown">
									<el-dropdown-item icon="el-icon-plus">0～60万</el-dropdown-item>
									<el-dropdown-item icon="el-icon-circle-plus">60～100万</el-dropdown-item>
									<el-dropdown-item icon="el-icon-circle-plus-outline">100～150万</el-dropdown-item>
									<el-dropdown-item icon="el-icon-check">150～200万</el-dropdown-item>
									<el-dropdown-item icon="el-icon-circle-check-outline">200～300万</el-dropdown-item>
									<el-dropdown-item icon="el-icon-circle-check-outline">300～500万</el-dropdown-item>
									<el-dropdown-item icon="el-icon-circle-check-outline">500万以上</el-dropdown-item>
								</el-dropdown-menu>
							</el-dropdown>
						</el-col>
					</div>
					<div class="bar_1">
						<div class="bar_1_1" id="show_area">
							<p style="margin-top: 32px;">面积：90-120平</p>
						</div>
						<div class="bar_1_2" id="area_detail">
							<div class="menu_price">
								<div class="price_radio" style="font-size: 15px;font-weight: 600;text-align: center;">
									选择面积：
								</div>
								<div class="price_radio">
									<el-radio v-model="radio1" label="area_buxian">面积不限</el-radio>
								</div>
								<div class="price_radio">
									<el-radio v-model="radio1" label="area1" class="price_radio">0～50平</el-radio>
								</div>
								<div class="price_radio">
									<el-radio v-model="radio1" label="area2" class="price_radio">50～70平</el-radio>
								</div>
								<div class="price_radio">
									<el-radio v-model="radio1" label="area3" class="price_radio">70～90平</el-radio>
								</div>
								<div class="price_radio">
									<el-radio v-model="radio1" label="area4" class="price_radio">90～120平</el-radio>
								</div>
								<div class="price_radio">
									<el-radio v-model="radio1" label="area5" class="price_radio">120～150平</el-radio>
								</div>
								<div class="price_radio">
									<el-radio v-model="radio1" label="area6" class="price_radio">150～200平</el-radio>
								</div>
								<div class="price_radio">
									<el-radio v-model="radio1" label="area7" class="price_radio">200平以上</el-radio>
								</div>
							</div>
							<div class="line"></div>
							<div class="zdy_price">
								<p class="zdy_text">自定义：</p>
								<input class="zdy_input"></el-input>
								<p class="zdy_text" style="margin-left: 5px;margin-right: 5px;"> ~ </p>
								<input class="zdy_input"></el-input>
								<button class="zdy_button">确定</button>
							</div>

						</div>
					</div>
					<div class="bar_1">
						<div class="bar_1_1" id="show_apartment">
							<p style="margin-top: 32px;">户型：两室</p>
						</div>
						<div class="bar_1_2" id="apartment_detail" style="height: 135px;width: 350px;">
							<div class="menu_price">
								<div class="price_radio" style="font-size: 15px;font-weight: 600;text-align: center;">
									选择面积：
								</div>
								<div class="price_radio">
									<el-radio v-model="radio2" label="apartment_buxian">居室不限</el-radio>
								</div>
								<div class="price_radio">
									<el-radio v-model="radio2" label="apartment1" class="price_radio">一室</el-radio>
								</div>
								<div class="price_radio">
									<el-radio v-model="radio2" label="apartment2" class="price_radio">两室</el-radio>
								</div>
								<div class="price_radio">
									<el-radio v-model="radio2" label="apartment3" class="price_radio">三室</el-radio>
								</div>
								<div class="price_radio">
									<el-radio v-model="radio2" label="apartment4" class="price_radio">四室</el-radio>
								</div>
								<div class="price_radio">
									<el-radio v-model="radio2" label="apartment5" class="price_radio">五室</el-radio>
								</div>
								<div class="price_radio">
									<el-radio v-model="radio2" label="apartment6" class="price_radio">五室以上</el-radio>
								</div>
							</div>
						</div>

					</div>
					<div class="bar_1">
						<div class="bar_1_1" id="show_region">
							<p style="margin-top: 32px;">楼层：高楼层</p>
						</div>
						<div class="bar_1_2" id="region_detail" style="height: 135px;width: 350px;">
							<!--动态添加区域-->
						</div>
					</div>
					<div class="bar_2">
						<p class="bar_2_1">标签：</p>
						<div class="bar_2_2">
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
							<p class="tip_1">默认</p>
						</div>
						<div class="tip">
							<p class="tip_1">单价</p>
							<div class="tip2">
								<i class="el-icon-caret-top"></i>
							</div>
							<div class="tip2" style="margin-top: 0px;">
								<i class="el-icon-caret-bottom"></i>
							</div>
						</div>
						<div class="tip">
							<p class="tip_1">总价</p>
							<div class="tip2">
								<i class="el-icon-caret-top"></i>
							</div>
							<div class="tip2" style="margin-top: 0px;">
								<i class="el-icon-caret-bottom"></i>
							</div>
						</div>
						<div class="tip">
							<p class="tip_1">面积</p>
							<div class="tip2">
								<i class="el-icon-caret-top"></i>
							</div>
							<div class="tip2" style="margin-top: 0px;">
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
	window.onload = function() {


		document.getElementById("show_area").onclick = function() {
			document.getElementById("area_detail").style.display = ((document.getElementById("area_detail").style.display ==
				'none') ? 'block' : 'none');
			document.getElementById("price_detail").style.display = "none";
			document.getElementById("apartment_detail").style.display = "none";
			document.getElementById("region_detail").style.display = "none";
		}

		document.getElementById("show_apartment").onclick = function() {
			document.getElementById("apartment_detail").style.display = ((document.getElementById("apartment_detail").style.display ==
				'none') ? 'block' : 'none');
			document.getElementById("area_detail").style.display = "none";
			document.getElementById("price_detail").style.display = "none";
			document.getElementById("region_detail").style.display = "none";
		}

		document.getElementById("show_region").onclick = function() {
			document.getElementById("region_detail").style.display = ((document.getElementById("region_detail").style.display ==
				'none') ? 'block' : 'none');
			document.getElementById("area_detail").style.display = "none";
			document.getElementById("apartment_detail").style.display = "none";
			document.getElementById("price_detail").style.display = "none";
		}

	}
	export default {
		data() {
			return {
				radio: '1',
				radio1: '1',
				radio2: '1'
			};
		},
		methods: {
			show_price() {
				document.getElementById("price_detail").style.display = ((document.getElementById("price_detail").style.display ==
					'none') ? 'block' : 'none');
				document.getElementById("area_detail").style.display = "none";
				document.getElementById("apartment_detail").style.display = "none";
				document.getElementById("region_detail").style.display = "none";
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
		width: 60px;
		height: 25px;
		background-color: rgb(226, 226, 226);
		margin-left: 10px;
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
