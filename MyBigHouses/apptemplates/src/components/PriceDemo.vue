<template>
	<div class="hello">
		<div class="charts">
<!-- 				<el-button type="primary" 
				:loading="loading_flag" 
				@click="getHisPrice_line(12)">过去一年</el-button>
				<el-button type="primary" 
				:loading="loading_flag" 
				@click="getHisPrice_line(36)">过去三年</el-button>
				<el-button type="primary" 
				:loading="loading_flag" 
				@click="getHisPrice_line(60)">过去五年</el-button>
				<el-button type="primary" 
				:loading="loading_flag" 
				@click="getHisPrice_line(100)">过去所有</el-button> -->
				
			<vue-highcharts :highcharts="Highcharts" 
			:options="options_chart_line" 
			ref="HisPriceCharts_line"></vue-highcharts>
			
			<vue-highcharts :highcharts="Highcharts" 
			:options="options_chart_line_tend" 
			ref="HisPriceCharts_line_tend"></vue-highcharts>
			
			<vue-highcharts :highcharts="Highcharts" 
			:options="options_chart_column" 
			ref="HisPriceCharts_column"></vue-highcharts>
			
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
				max_lenght_tend: 0,
				options_chart_line: {
					chart: {
						zoomType: 'x',
						type:'spline'
					},
					title: {
						text: '房价走势图'
					},
					subtitle: {
						text: '数据来源: anjuke.com'
					},
					xAxis: {
						// categories: ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月']
					},
					yAxis: {
						title: {
							text: '价格 (元/平方米)'
						},
						labels: {
							formatter: function () {
								return this.value + '元/平方米';
							}
						}
					},
					plotOptions: {
						series: {
							cursor: 'pointer',
							point: {
							},
							marker: {
								lineWidth: 1
							}
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
					
					//去除水印
					credits: {
						enabled: false
					},
					series: [
					]
				},
				options_chart_line_tend: {
					chart: {
						zoomType: 'x',
						type:'line'
					},
					title: {
						text: '房价趋势图'
					},
					subtitle: {
						text: '数据来源: anjuke.com'
					},
					xAxis: {
						// categories: ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月']
					},
					yAxis: {
						title: {
							text: '趋势 (百分比%)'
						},
						labels: {
							formatter: function () {
								return this.value + '%';
							}
						}
					},
					plotOptions: {
						series: {
							cursor: 'pointer',
							point: {
							},
							marker: {
								lineWidth: 1
							}
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
					
					//去除水印
					credits: {
						enabled: false
					},
					series: [
					]
				},
				options_chart_column:{
					chart: {
						type:'column'
					},
					title: {
						text: '房价趋势图'
					},
					subtitle: {
						text: '数据来源: anjuke.com'
					},
					xAxis: {
						// categories: ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月']
					},
					yAxis: {
						title: {
							text: '价格 (元/平方米)'
						},
						labels: {
							formatter: function () {
								return this.value + '元/平方米';
							}
						}
					},
					tooltip:{
						headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
						  pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td><td style="padding:0"><b>{point.y:.1f} 元/平方米</b></td></tr>',
						  footerFormat: '</table>',
						  shared: true,
						  useHTML: true
					},
					plotOptions: {
						column: {
							 pointPadding: 0.2,
							 borderWidth: 0
						  }
					},
					//去除水印
					credits: {
						enabled: false
					},
					series: [
					]
				}
			}
		},
		mounted() {
			// console.log(store.state.area_eng.city);
			this.getHisPrice_line(12, store.state.area_eng.city)
			this.getHisPrice_line_tend(12, store.state.area_eng.city)
			this.getHisPrice_coloumn(3, store.state.area_eng.city)
		},
		methods: {
			getHisPrice_line(last_n_month=12, choosed_city='suzhou') {
				// console.log(choosed_city)
				// button是否正在加载
				this.loading_flag = true
				// 是否缩放
				var shrink_flag = false
				this.$ajax({
					method: 'get',
					// url: 'http://127.0.0.1:8000/house/history/' + store.state.city + '?last_n_month='+last_n_month+'/'
					url: 'http://127.0.0.1:8000/house/price/'+choosed_city+'/history?last_n_month='+last_n_month
				}).then(function(response) {
					if (response.data.code === 0) {
						// 获得chart
						let his_chart = this.$refs.HisPriceCharts_line
						// 加载highchart自带的方法
						// his_chart.delegateMethod('get', 'showLoading', 'Loading...')
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
			},
			getHisPrice_line_tend(last_n_month=12, choosed_city='suzhou') {
				// button是否正在加载
				this.loading_flag = true
				// 是否缩放
				var shrink_flag = false
				this.$ajax({
					method: 'get',
					// url: 'http://127.0.0.1:8000/house/history/' + store.state.city + '?last_n_month='+last_n_month+'/'
					url: 'http://127.0.0.1:8000/house/price/'+choosed_city+'/history?last_n_month='+last_n_month
				}).then(function(response) {
					if (response.data.code === 0) {
						// 获得chart
						let his_chart = this.$refs.HisPriceCharts_line_tend
						// 加载highchart自带的方法
						// his_chart.delegateMethod('get', 'showLoading', 'Loading...')
						// 接受get请求返回的数据
						let hist_price = []
						let x_axis = []
						// console.log(response.data.data)
						for (let s of response.data.data) {
							hist_price.push(parseFloat(s[2]))
							x_axis.push(s[0])
						}
						// 如果返回的数据较长，则扩充x轴长度并对列表中的原数据进行pad
						if(parseInt(response.data.count) > this.max_lenght_tend){
							this.max_lenght_tend = parseInt(response.data.count)
							his_chart.getChart().xAxis[0].setCategories(x_axis)
							for(var i = 0; i < his_chart.getChart().series.length; i++){
								var series_now = his_chart.getChart().series[i]
								var temp = []
								for(var j = 0; j < this.max_lenght_tend-series_now.data.length; j++){
									temp.push(null)
								}
								for(var j of series_now.data){
									temp.push(j.y)
								}
								series_now.setData(temp)
							}
						}else{ // 如果长度更短则对请求返回的数据进行pad
							shrink_flag = true
							for(var i = 0; i < this.max_lenght_tend-parseInt(response.data.count); i++){
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
							this.max_lenght_tend = new_length
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
			},
			getHisPrice_coloumn(last_n_month=1, choosed_city='suzhou'){
				this.loading_flag = true
				// 是否缩放
				this.$ajax({
					method: 'get',
					// url: 'http://127.0.0.1:8000/house/history/' + store.state.city + '?last_n_month='+last_n_month+'/'
					url: 'http://127.0.0.1:8000/house/price/'+choosed_city+'/sub_location?last_n_month='+last_n_month
				}).then(function(response) {
					if (response.data.code === 0) {
						// 获得chart
						let his_chart = this.$refs.HisPriceCharts_column
						// 加载highchart自带的方法
						// his_chart.delegateMethod('get', 'showLoading', 'Loading...')
						// 接受get请求返回的数据
						let hist_price_list = []
						let x_axis = []
						for(let i = last_n_month-1; i >=0; i--){
							let hist_price = []
							for (let s of response.data.data[i]) {
								// console.log(s)
								hist_price.push(parseFloat(s[1]))
								if(i == 0){
									x_axis.push(s[0])
								}
							}
							// hist_price_list.push(hist_price)
							// 添加数据
							// console.log(response.data.location_cn)
							his_chart.addSeries({
								id: choosed_city,
								name:response.data.time[i],
								data:hist_price,
							})
						}
						his_chart.getChart().xAxis[0].setCategories(x_axis)
						
					} else {
						alert(response.data.msg)
					}
					this.loading_flag = false
				}.bind(this))
			}
		},
		
		components: {
			VueHighcharts
		}
	}
</script>
