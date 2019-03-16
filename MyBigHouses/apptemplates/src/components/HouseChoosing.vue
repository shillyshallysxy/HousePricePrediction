<template>
	<div class="body">
		<div class="choose_body">
			<div class="Content">
				<div class="bar">
					<div class="bar_1">
						<p class="bar_1_1">总价：200-400万</p>
					</div>
					<div class="bar_1">
						<p class="bar_1_1">面积：90-120平</p>
					</div>
					<div class="bar_1">
						<p class="bar_1_1">户型：两室一厅</p>
					</div>
					<div class="bar_1">
						<p class="bar_1_1">楼层：高楼层</p>
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
</script>

<style scoped>
.body{
	width: 100%;
	height: 1000px;
	min-width: 1273px;
}
.choose_body{
	width: 100%;
	height: 1000px;
	background-color: white;
	padding-left: 50%;
}
.Content{
	width: 950px;
	height: 950px;
	margin-left: -475px;
	padding-top: 50px;
}
.bar{
	width: 100%;
	height: 220px;
	border: 1px solid rgb(237,237,237);
	border-top: 5px solid #009688;
	background-color: white;
}
.bar_1{
	width: 200px;
	height: 100px;
	border: 1px solid rgb(224,224,224);
	background-color: rgb(249,249,249);
	margin-left: 30px;
	margin-top: 30px;
	float: left;
	border-radius: 20px;
}
.bar_1_1{
	font-size: 20px;
	margin-top: 32px;	
}
.bar_2{
	width: 100%;
	height: 50px;
	margin-top: 150px;
}
.bar_2_1{
	float: left;
	font-family: "黑体";
	font-size: 20px;
	font-weight: 400;
	margin-top: 10px;
	margin-left: 30px;
}
.bar_2_2{
	/*未选中*/
	width: 60px;
	height: 25px;
	background-color: rgb(226,226,226);
	margin-left: 10px;
	margin-top: 12px;
	float: left;
	border-radius: 5px;
	padding: 1px;
}
.bar_2_3{
	/*已选中*/
	width: 60px;
	height: 25px;
	background-color: rgb(200,200,200);
	margin-left: 10px;
	margin-top: 12px;
	float: left;
	border-radius: 5px;
	padding: 1px;
}
.bar_2_4{
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
.bar_2_5{
	font-size: 10px;
	font-weight: 500;
	margin-top: 3px;
}
.middle{
	width: 100%;
	height: 100px;
	border: 0px;
	padding-top: 1px;
}
.middle1{
	width: 20px;
	height: 50px;
	border: 0px;
	background-color: rgb(154,154,154);
	margin-top: 30px;
	float: left;
}
.middle2{
	font-size: 24px;
	float: left;
	margin-top: 40px;
	margin-left: 20px;
}
.tips{
	width: 100%;
	height: 100px;
	border: 0px;	
}
.tip{
	width: 100px;
	height: 40px;
	background-color: white;
	border: 1px solid rgb(224,224,224);
	background-color: rgb(249,249,249);
	border-top: 5px solid #009688;
	float: left;
}
.tip_1{
	font-size: 15px;
	margin-top: 6px;
	float: left;
	margin-left: 20px;
}
.tip2{
	float: right;
	width: 20px;
	height: 10px;
	margin-top: 4px;
	margin-right: 8px;
}
.list{
	width: 100%;
	height: 530px;
	border: 0px;
}

</style>
