<template>
	<div style="background-color: white;width: 100%;height: 200px;margin: 0;padding: 0;min-width: 1050px;">
		<div style="background-color: white; width: 100%;height: 183px;;margin: 0;padding: 0;display:block;">
			<img src="../assets/logo1.png" style="max-height: 40px;float: left;margin-left: 16%;margin-top: 40px;"/>
			<p style="float:left;font-size: 20px;color: black;font-weight: 700;margin-left: 10px;margin-top: 45px;">
				My Big Houses
			</p>
			
			<table style="border: #000000;width: 50%;">
				<tr>
					<td>关于MBH</td>
					<td>隐私声明</td>
					<td>Blog</td>
				</tr>
				<tr>
					<td>联系我们</td>
					<td>合作与友情链接</td>
					<td>FAQ</td>
				</tr>
				<tr>
					<td>加入我们</td>
					<td>服务条款</td>
					<td>意见反馈</td>
				</tr>
			</table>
		</div>
		<el-menu router :default-active="$route.path" class="el-menu-demo" mode="horizontal" @select="handleSelect" background-color="#009688" text-color="#fff" active-text-color="#ffd04b" >
		<p style="margin-left: 10%;font-size: 10px;float: left;color: white;">
			Copyright 2019.All right reserved.
		</p>
		<p style="margin-right: 10%;font-size: 10px;float: right;color: white">
			China:=86 1 22 33 44 55 MBH@shark.com
		</p>
		</el-menu>
	</div>
</template>

<script>
</script>

<style scoped>
table,th,td{
  border: 0px solid black;
}
table{
	margin-top: 70px;
	margin-left: 50px;
}
tr{
	margin-top: 30px;
}
td{
	height: 30px;
	font-size: 15px;
	font-weight: 400;
}
</style>
