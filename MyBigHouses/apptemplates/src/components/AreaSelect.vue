<template>
	<div style="width: 100%; height:800px; min-width:1320px; margin-top: 60px;">
		<span class="demonstration" style="font-size: 18px;">请选择你所在的城市</span>
		<el-cascader placeholder="试试搜索：指南" :options="options" filterable style="margin-left: 60px;"></el-cascader>
	</div>
</template>

<script>
	export default {
		data() {
			return {
				options: [{
						value: 'jiangsu',
						label: '江苏',
						children: [{
							value: 'changzhou',
							label: '常州'
						}, {
							value: 'dafeng',
							label: '大丰'
						}, {
							value: 'huaian',
							label: '淮安'
						}, {
							value: 'kunshan',
							label: '昆山'
						}, {
							value: 'lianyungang',
							label: '连云港'
						}, {
							value: 'nanjing',
							label: '南京'
						}, {
							value: 'nantong',
							label: '南通'
						}, {
							value: 'shuyang',
							label: '沭阳'
						}, {
							value: 'suqian',
							label: '宿迁'
						}, {
							value: 'suzhou',
							label: '苏州'
						}, {
							value: 'taicang',
							label: '太仓'
						}, {
							value: 'taizhou',
							label: '泰州'
						}, {
							value: 'wuxi',
							label: '无锡'
						}, {
							value: 'xuzhou',
							label: '徐州'
						}, {
							value: 'yancheng',
							label: '盐城'
						}, {
							value: 'yangzhou',
							label: '扬州'
						}, {
							value: 'zhenjiang',
							label: '镇江'
						}, ]
					},
					{
						value: 'guangxi',
						label: '广西',
						children: [{
							value: 'baise',
							label: '百色'
						}, {
							value: 'beihai',
							label: '北海'
						}, {
							value: 'chongzuo',
							label: '崇左'
						}, {
							value: 'fangchenggang',
							label: '防城港'
						}, {
							value: 'guigang',
							label: '贵港'
						}, {
							value: 'guilin',
							label: '桂林'
						}, {
							value: 'hechi',
							label: '河池'
						}, {
							value: 'hezhou',
							label: '贺州'
						}, {
							value: 'laibin',
							label: '来宾'
						}, {
							value: 'liuzhou',
							label: '柳州'
						}, {
							value: 'nanning',
							label: '南宁'
						}, {
							value: 'qinzhou',
							label: '钦州'
						}, {
							value: 'wuzhou',
							label: '梧州'
						}, {
							value: 'yulin',
							label: '玉林'
						}, ]
					},
					
					
					
					
					

				]
			};
		}
	};
</script>

<style>

</style>
