<template>
	<div class="body" v-loading.fullscreen.lock="fullscreenLoading">
		<div class="bar"></div>
		<div class="PredictiveContent">
			<div class="Content">
				<div class="main_first">
					<div class="main_left">
						<div class="main_left_1">
							<div class="circle1"></div>
							<div class="circle2" style="margin-top:150px;"></div>
							<div class="circle2" style="margin-top:150px;"></div>
							<div class="circle1" style="margin-top:150px;"></div>
							<div class="circle1" style="margin-top:150px;"></div>
						</div>
						<div class="main_left_2">
							<div class="left_part_1">
								预测三个月后房价：
							</div>
							<div class="left_part_1">
								{{predict_info.three_month_later}}
							</div>
							<div class="left_part_2" style="margin-top: 60px;">
								预测一个月后房价：
							</div>
							<div class="left_part_2" style="color: red;">
								{{predict_info.one_month_later}}
							</div>
							<div class="left_part_2" style="margin-top: 60px;">
								当前房价：
							</div>
							<div class="left_part_2">
								{{predict_info.present}}
							</div>
							<div class="left_part_1" style="margin-top: 60px;">
								一个月前房价：
							</div>
							<div class="left_part_1">
								{{predict_info.one_month_earlier}}
							</div>
							<div class="left_part_1" style="margin-top: 60px;">
								半年前房价：
							</div>
							<div class="left_part_1">
								{{predict_info.half_year_earlier}}
							</div>
						</div>
					</div>

					<div class="main_right">
						<div class="right_1" style="margin-top: 70px;">
							本月实际价格
						</div>
						<div class="right_2">
							与
						</div>
						<div class="right_1">
							上个月预测价格
						</div>
						<div class="right_2">
							误差
						</div>
						<div class="right_1" style="font-size: 32px;">
							{{predict_info.error}} 元
						</div>
					</div>
					<div class="main_right_1" style="padding-top: 40px;">
						<vue-highcharts :highcharts="Highcharts" :options="options_chart_line" ref="HisPriceCharts_line"></vue-highcharts>
					</div>

				</div>
				<div class="main_second">
					<div class="main_second_left">
						<div class="main_second_left_1" v-for="(o, index) in news_info" style="margin-top: 50px;" key="index" @click="change_news(index)">{{o.title}}</div>

					</div>
					<div class="main_second_middle">
					</div>
					<div class="main_second_right" id='main_second_right' v-html="html">

					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import global_ from '@/components/Global'
	import store from '@/store'
	import iView from 'iview'
	import Vue from 'vue'
	import VueHighcharts from 'vue2-highcharts'
	import HighCharts from 'highcharts'
	export default {
		data() {
			return {
				// 默认无数据
				predict_info: {
					present: '无数据',
					one_month_later: '无数据',
					one_month_earlier: '无数据',
					half_year_earlier: '无数据',
					three_month_later: '无数据',
					error:'无数据'
				},
				news_info: [],
				html: '',
				// 折线图当前选择的城市
				city_selected: [],
				// 存储折线图的数据
				his_price_line: {},
				// 存储x轴信息
				x_axis_line: [],
				id: 'history_price',
				// 折线图charts的初始设置
				options_chart_line: {
					chart: {
						zoomType: 'x',
						type: 'spline',
						backgroundColor: "#ffffff",
						borderRadius: "2",
						// shadow: true
					},
					title: {
						text: "房价走势预测图"
					},
					subtitle: {},
					xAxis: {},
					yAxis: {
						title: {
							text: '价格 (元/平方米)'
						},
						labels: {
							formatter: function() {
								return this.value;
							}
						}
					},
					plotOptions: {
						series: {
							cursor: 'pointer',
							point: {},
							marker: {
								lineWidth: 1
							},
							zoneAxis: 'x',
							// 设置预测颜色
							zones: [{
								value: 5,
								color: '#7cb5ec',
							}, {
								value: 9,
								dashStyle: 'ShortDashDotDot',
								color: '#f7a35c',
							}]
						},
						line: {
							dataLabels: {
								// 开启数据标签
								enabled: true
							},
							// 关闭鼠标跟踪，对应的提示框、点击事件会失效
							enableMouseTracking: true
						}
					},
					credits: {
						enabled: false
					},
					style: {
						fontFamily: "",
						fontSize: '12px',
						fontWeight: 'bold',
						color: '#e8e8e8'
					},
					series: []
				},
			}
		},
		mounted() {
			this.get_news_info()
			this.get_price_info()
			this.city_name_cn = store.state.area.city
			this.city_name_en = store.state.area_eng.city
			// 更新当前选择的城市
			this.city_selected = [store.state.area_eng.province, store.state.area_eng.city]
			// 更新折线图图表
			this.getSelectedCityPrice()
		},
		components: {
			VueHighcharts
		},
		methods: {
			// 更改曲线图的城市,并同步更新曲线图
			getSelectedCityPrice() {
				var city_sel_len = this.city_selected.length
				if (city_sel_len == 0) {
					iView.Message.info('请选择城市')
				} else if (city_sel_len == 1) {
					iView.Message.info('请选择继续选择下一级')
				} else {
					var city_now = this.city_selected[city_sel_len - 1]
					this.getHisPrice_line_data(city_now)
				}
			},
			// 异步请求获取曲线图的数据
			getHisPrice_line_data(choosed_city) {
				// 默认获取获取数据长度为9
				let last_n_month = 9
				this.$ajax({
					method: 'get',
					url: global_.IpUrl + '/house/predict/' + choosed_city
				}).then(function(response) {
					// 成功返回数据则进入该方法, 否则弹出失败信息
					if (response.data.code === 0) {
						// 判断是否已经加载过该地区的折线图数据了，如果未加载过则加载
						if (typeof(this.his_price_line[choosed_city]) == 'undefined') {
							let hist_price = []
							let x_axis = []
							// 接受get请求返回的数据
							for (let s of response.data.chart_data) {
								if (hist_price.length == 5) {
									hist_price.push({
										'y': parseFloat(s[1]),
										'color': '#7cb5ec'
									})
								} else {
									hist_price.push(parseFloat(s[1]))
								}
								x_axis.push(s[0])
							}
							//console.log(hist_price)
							// 如果返回的数据较短，则扩充x轴长度并对列表中的原数据进行pad
							if (parseInt(response.data.chart_data.length) < last_n_month) {
								for (var i = 0; i < last_n_month - parseInt(response.data.chart_data.length); i++) {
									hist_price.unshift(null)
								}
							} else {
								this.x_axis_line = x_axis
							}
							// 将获取的数据更新
							this.his_price_line[choosed_city] = hist_price
						}
						// 更新表格（chart）
						this.showCart()
					} else {
						iView.Message.info(response.data.msg)
					}
				}.bind(this))
			},
			// 更新chart的方法
			showCart() {
				let last_n_month = 9
				// 获得chart
				let his_chart = this.$refs.HisPriceCharts_line
				// 更新x轴
				his_chart.getChart().xAxis[0].setCategories(this.x_axis_line.slice(-last_n_month))
				for (var hist_price_key in this.his_price_line) {
					var vali_series = his_chart.getChart().get(hist_price_key)
					// 如果表格中不存在该数据则加入该数据
					if (typeof(vali_series) == "undefined") {
						his_chart.addSeries({
							id: hist_price_key,
							name: hist_price_key,
							data: this.his_price_line[hist_price_key].slice(-last_n_month),
						})
						// 如果表格中存在该数据则更新该数据
					} else {
						vali_series.setData(this.his_price_line[hist_price_key].slice(-last_n_month))
					}
				}
			},
			//点击信息跳转详情
			change_news(index) {
				this.html = this.news_info[index].body
			},
			//获取当前城市的新闻信息
			get_news_info() {
				var _this = this
				const loading = this.$loading({
					lock: true,
					text: 'Loading',
					spinner: 'el-icon-loading',
					background: 'rgba(255,255,255,0.8)'
				});
				_this.$ajax({
					url: global_.IpUrl + '/house/news/' + this.get_city,
					methods: 'get'
				}).then(function(response) {
					loading.close();
					if (response.data.code === 0 && response.data.count != 0) {
						var news = response.data.data
						_this.news_info = []
						_this.html = news[0].body
						for (var i = 0; i < news.length; i++) {
							var temp_news = {}
							temp_news["title"] = news[i].title
							temp_news["source"] = news[i].source
							temp_news["pub_date"] = news[i].pub_date
							temp_news["body"] = news[i].body
							_this.news_info.push(temp_news)
						}
					} else {

					}

				})

			},
			//获取当前城市的过去以及将来的预测房价
			get_price_info() {
				var _this = this
				_this.$ajax({
					url: global_.IpUrl + '/house/predict/' + this.get_city_eng,
					methods: 'get'
				}).then(function(response) {
					if (response.data.code === 0) {
						var temp_predict_info = response.data.data
						_this.predict_info.present = temp_predict_info[2]
						_this.predict_info.one_month_later = temp_predict_info[3]
						_this.predict_info.one_month_earlier = temp_predict_info[1]
						_this.predict_info.half_year_earlier = temp_predict_info[0]
						_this.predict_info.three_month_later = temp_predict_info[4]
						_this.predict_info.error = response.data.error
					} else {
						iView.$Message.info(response.data.msg)
					}
				})
			}
		},
		computed: {
			//获取城市中文
			get_city() {
				return store.state.area.city
			},
			//获取城市拼音
			get_city_eng() {
				return store.state.area_eng.city
			}
		}
	}
</script>

<style scoped>
	.body {
		width: 100%;
		height: 1400px;
		min-width: 1050px;
	}

	.bar {
		min-width: 100%;
		height: 10px;
		background-color: rgb(237, 237, 237);
	}

	.PredictiveContent {
		margin-top: 30px;
		width: 100%;
		height: 1400px;
		background-color: white;
		padding-left: 50%;
	}

	.Content {
		width: 950px;
		height: 1350px;
		margin-left: -475px;
		padding-top: 30px;
	}

	.main_first {
		width: 100%;
		height: 800px;
		background: white;
		float: left;
	}

	.main_left {
		width: 430px;
		height: 100%;
		float: left;
	}

	.main_left_1 {
		width: 2px;
		height: 90%;
		background-color: rgba(210, 236, 233, 100);
		margin-left: 20%;
		float: left;
	}

	.circle1 {
		width: 20px;
		height: 20px;
		background: rgba(0, 150, 136, 100);
		-moz-border-radius: 10px;
		-webkit-border-radius: 10px;
		border-radius: 10px;
		margin-left: -9px;
	}

	.circle2 {
		width: 30px;
		height: 30px;
		background: rgba(255, 152, 0, 100);
		-moz-border-radius: 15px;
		-webkit-border-radius: 15px;
		border-radius: 15px;
		margin-left: -14px;
	}

	.main_left_2 {
		width: 250px;
		height: 90%;
		margin-left: 10%;
		float: left;
	}

	.left_part_1 {
		width: 200px;
		height: 50px;
		color: black;
		text-align: left;
		font-size: 16px;
	}

	.left_part_2 {
		width: 200px;
		height: 50px;
		color: black;
		text-align: left;
		font-size: 20px;
	}

	.main_right {
		width: 500px;
		height: 360px;
		margin-left: 20px;
		float: left;
		background: rgba(210, 236, 233, 100);
		border-radius: 60px;
	}

	.main_right_1 {
		width: 520px;
		height: 440px;
		float: left;
	}

	.right_1 {
		font-size: 24px;
		margin-top: 10px;
		color: black;
	}

	.right_2 {
		margin-top: 10px;
		font-size: 20px;
		color: black;
	}

	.main_second {
		width: 100%;
		height: 500px;
		background: white;
		border-radius: 30px;
		margin-top: 830px;
		background-color: rgb(237, 237, 237);
	}

	.main_second_left {
		width: 300px;
		height: 100%;
		float: left;
	}

	.main_second_left_1 {
		cursor: pointer;
		padding-top: 15px;
		font-size: 15px;
		width: 200px;
		margin-left: 50px;
		height: 100px;
		border-bottom: 1px solid darkgray;
	}

	.main_second_middle {
		width: 10px;
		height: 80%;
		margin-top: 50px;
		border-left: 1px solid darkgray;
		float: left;
	}

	.main_second_right {
		width: 500px;
		height: 80%;
		margin-left: 50px;
		margin-top: 50px;
		float: left;
		overflow: auto;
	}
</style>
