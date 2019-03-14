<template>
	<div class="body">
		<div class="bar"></div>
		<div class="PredictiveContent">
			<div class="Content">
				<div class="main_first">
					<div class="main_left">
						<div class="main_left_1">
							<p class="left_part_1">苏州</p>
						</div>
						<div class="main_left_2">
							<div class="left_part_2">
								<p class="left_part_2_1">
									当前房价
								</p>
								<p class="left_part_2_2">
									45678
								</p>
								<p class="left_part_2_3">元</p>				
							</div>
							<div class="left_part_2">
								<p class="left_part_2_1">
									预测1个月后房价
								</p>
								<p class="left_part_2_2">
									45678
								</p>
								<p class="left_part_2_3">元</p>
							</div>
						</div>
						<div class="main_left_3">
							<div class="left_part_3" style="border-left: 0;">
								<p class="left_part_3_1">
									一个月前房价
								</p>
								<p class="left_part_3_2">
									45678
								</p>
							</div>
							<div class="left_part_3">
								<p class="left_part_3_1">
									半年前房价
								</p>
								<p class="left_part_3_2">
									45678
								</p>
							</div>
							<div class="left_part_3">
								<p class="left_part_3_1">
									预测3个月后房价
								</p>
								<p class="left_part_3_2">
									45678
								</p>
							</div>
						</div>
					</div>
					<div class="main_right"></div>
				</div>
				<div class="main_second">
					<div class="main_second_left">
						<div class="main_second_left_1" style="margin-top: 50px;"></div>
						<div class="main_second_left_1"></div>
						<div class="main_second_left_1"></div>
						<div class="main_second_left_1" style="border-bottom: 0px;"></div>
					</div>
					<div class="main_second_middle">	
					</div>
					<div class="main_second_right">	
					</div>
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
.bar{
	min-width: 100%;
	height: 60px;
	background-color: rgb(237,237,237);
}
.PredictiveContent{
	width: 100%;
	height: 1000px;
	background-color: white;
	padding-left: 50%;
}
.Content{
	width: 950px;
	height: 950px;
	margin-left: -475px;
	padding-top: 30px;
}
.main_first{
	width: 100%;
	height: 400px;
	background: white;
	float: left;
}
.main_left{
	width: 550px;
	height: 100%;
	background-color: rgb(17,134,117);
	float: left;
}
.main_left_1{
	width: 100%;
	height: 45%;
}
.main_left_2{
	width: 100%;
	height: 30%;
}
.left_part_1{
	font-size: 48px;
	font-weight: 600;
	float: left;
	margin-left: 30px;
	margin-top: 30px;
	color: white;
}
.left_part_2{
	width: 50%;
	height: 100%;
	float: left;
	text-align: center;
}
.left_part_2_1{
	font-size: 20px;
	font-weight: 600;
	font-family: arial;
	color: white;
}
.left_part_2_2{
	margin-left: 60px;
	font-size: 48px;
	font-weight: 600;
	font-family: arial;
	color: white;
	float: left;
}
.left_part_2_3{
	margin-top: 20px;
	font-size: 32px;
	font-weight: 400;
	color: white;
	float: left;
}
.main_left_3{
	width: 100%;
	height: 25%;
	background-color: white;
	border: 1px solid black;
}
.left_part_3{
	width: 33%;
	height: 100%;
	float: left;
	border-left: 1px solid black;
	text-align: center;
}
.left_part_3_1{
	margin-top: 20px;
	font-size: 20px;
	font-weight: 600;
	font-family: arial;
	color: black;
}
.left_part_3_2{
	font-size: 20px;
	font-weight: 600;
	font-family: arial;
	color: black;
}
.main_right{
	width: 350px;
	height: 100%;
	margin-left: 50px;
	border: 1px solid black;
	float: left;
}
.main_second{
	width: 100%;
	height: 500px;
	background: white;
	border-radius: 30px;
	margin-top: 430px;
	background-color: rgb(237,237,237);
}
.main_second_left{
	width: 300px;
	height: 100%;
	float: left;
}
.main_second_left_1{
	width: 200px;
	margin-left: 50px;
	height: 100px;
	border-bottom: 1px solid darkgray;
}
.main_second_middle{
	width: 10px;
	height: 60%;
	margin-top: 100px;
	border-left: 1px solid darkgray;
	float: left;
}
.main_second_right{
	width: 500px;
	height: 80%;
	margin-left: 50px;
	margin-top: 50px;
	background-color: white;
	float: left;
}
</style>
