<template>
	<div class="body"  v-loading.fullscreen.lock="fullscreenLoading">
		<div class="choose_body">
			<div class="Content">
				<div class="middle">
					<div class="middle1"></div>
					<p class="middle2">查询结果</p>
				</div>
				
				<div class="list_content">
					<ul class="list">
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
									单价：{{o.price}}万
								</p>
								<p style="font-size: 12px;font-weight: 300;margin-top: 20px;">
									{{o.star_count}}人已收藏
								</p>
							</div>
							<div class="line1"></div>
						</li>
					</ul>
					<v-pagination :total="total" :current-page='current' @pagechange="pagechange"></v-pagination>	
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
		components: {
			'v-pagination': pagination,
		},
		data() {
			return {
				favor_info: [],
				//分页实现内容
				total: 0, // 记录总条数
				display: 15, // 每页显示条数
				current: 1, // 当前的页数
			};
		},
		mounted() {
			var search_info = this.$route.query.search_info
			var _this = this
			_this.$ajax({
				url:global_.IpUrl+"/house/search/?page="+this.current+"&text="+search_info,
				
			})
		},
		methods: {
			
			pagechange(page) {
				this.current = page
				
				if(this.istrue){
					this.get_select_List()
					document.documentElement.scrollTop=0
				}else{
					this.get_default_list()
					document.documentElement.scrollTop=0
				}
				
			},
			
			
			
		},
		computed: {
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
