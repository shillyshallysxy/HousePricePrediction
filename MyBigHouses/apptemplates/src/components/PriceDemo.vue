<template>
	<div class="hello">
		<div class="charts">
			<div class="block">
				<el-button type="primary" :loading="loading_flag" @click="getHisPrice(12)">过去一年</el-button>
				<el-button type="primary" :loading="loading_flag" @click="getHisPrice(36)">过去三年</el-button>
				<el-button type="primary" :loading="loading_flag" @click="getHisPrice(60)">过去五年</el-button>
				<el-button type="primary" :loading="loading_flag" @click="getHisPrice(100)">过去所有</el-button>
				
			<vue-highcharts :highcharts="Highcharts" :options="options_chart" ref="HisPriceCharts"></vue-highcharts>
		</div>
		<span>{{from_ymonth}}</span><span>{{to_ymonth}}</span>
	</div>
</template>

<script>
	// 导入chart组件
	import VueHighcharts from 'vue2-highcharts'
	import HighCharts from 'highcharts'
	import store from '@/store'
	export default {
		store,
		data() {
			return {
				loading_flag: false,
				id: 'history_price',
				max_length: 0,
				options_chart: {
					chart: {
						zoomType: 'x',
						type:'spline'
					},
					title: {
						text: '房价趋势图'
					},
					subtitle: {
						// text: '数据来源: WorldClimate.com'
					},
					xAxis: {
						categories: ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月']
					},
					yAxis: {
						title: {
							text: '价格 (元/平方米)'
						}
					},
					plotOptions: {
						line: {
							dataLabels: {
								// 开启数据标签
								enabled: true
							},
							// 关闭鼠标跟踪，对应的提示框、点击事件会失效
							enableMouseTracking: true
						}
					},
					//去除水印
					credits: {
						enabled: false
					},
					series: [
					]
				},
				options_city:{
					
				}
			}
		},
		mounted() {
// 			console.log(store.state.isLogin);
// 			console.log(store.state.UserInfo.username);
			this.getHisPrice(12, 'suzhou')
		},
		methods: {
			getHisPrice(last_n_month, choosed_city='suzhou') {
				// button是否正在加载
				this.loading_flag = true
				// 是否缩放
				var shrink_flag = false
				this.$ajax({
					method: 'get',
					// url: 'http://127.0.0.1:8000/house/history/' + store.state.city + '?last_n_month='+last_n_month+'/'
					url: 'http://127.0.0.1:8000/house/history/'+choosed_city+'?last_n_month='+last_n_month
				}).then(function(response) {
					if (response.data.code === 0) {
						// 获得chart
						let his_chart = this.$refs.HisPriceCharts
						// 加载highchart自带的方法
						his_chart.delegateMethod('get', 'showLoading', 'Loading...')
						// 接受get请求返回的数据
						let hist_price = []
						let x_axis = []
						for (let s of response.data.data) {
							hist_price.push(parseFloat(s[1]))
							x_axis.push(s[0])
						}
						// 如果返回的数据较长，则扩充x轴长度并对列表中的原数据进行pad
						if(parseInt(response.data.count) > this.max_length){
							this.max_length = parseInt(response.data.count)
							his_chart.getChart().xAxis[0].setCategories(x_axis)
							for(var i = 0; i < his_chart.getChart().series.length; i++){
								var series_now = his_chart.getChart().series[i]
								var temp = []
								for(var j = 0; j < this.max_length-series_now.data.length; j++){
									temp.push(null)
								}
								for(var j of series_now.data){
									temp.push(j.y)
								}
								series_now.setData(temp)
							}
						}else{ // 如果长度更短则对请求返回的数据进行pad
							shrink_flag = true
							for(var i = 0; i < this.max_length-parseInt(response.data.count); i++){
								hist_price.unshift(null)
							}
						}
						// 添加数据 如果存在则update如果不存在则add
						var vali_series = his_chart.getChart().get(choosed_city)
						if(typeof(vali_series) == "undefined"){
							his_chart.addSeries({
								id: choosed_city,
								name:response.data.city,
								data:hist_price,
							})
						}else{
							vali_series.setData(hist_price)
						}
						// 如果缩放的是原数据，则对chart进行更新
						if(shrink_flag){
							// 获得更新之后图标中最长的数据
							var new_length = 0
							for(var i = 0; i < his_chart.getChart().series.length; i++){
								var series_now_data = his_chart.getChart().series[i].data
								var count_i = 0
								for(let j of series_now_data){
									if(j.isNull){
										count_i++
									}
								}
								var series_now_length = series_now_data.length-count_i
								if(new_length < series_now_length){
									new_length = series_now_length
								}
							}
							this.max_length = new_length
							// 对其他数据接触过多的pad
							for(var i = 0; i < his_chart.getChart().series.length; i++){
								var series_now = his_chart.getChart().series[i]
								his_chart.getChart().series[i].setData(series_now.data.slice(series_now.data.length-this.max_length))
							}
						}
					} else {
						alert(response.data.msg)
					}
					this.loading_flag = false
				}.bind(this))
			}
		},
		computed:{
			getCityInfo(){
				return store.state.area.city
			}
		},
		components: {
			VueHighcharts
		}
	}
</script>
