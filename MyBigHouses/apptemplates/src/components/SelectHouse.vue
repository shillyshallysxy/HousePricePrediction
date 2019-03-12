<template>
	<div id="selecthouse" style="margin-top: 60px ;">
		<div id="selectcard">

		</div>
		<div id='selectconsequence' style="background-color: #2BAEE9; width: 70%; margin: 0,auto; display: inline-block;">
			<span>查询结果</span>
			<el-row>
				<el-col :span="8" v-for="(o, index) in ShowHouse" :key="o" :offset="index > 0 ? 2 : 0" style="margin-bottom: 2.5rem;margin-left:30px ;width: 182px;height: 250px;">
					<el-card :body-style="{ padding: '0px', height:'250px'}" style="width: 180px;">
						<img src="../assets/2.jpg" class="image" >
						<div style="padding: 14px;">
							<span>好吃的汉堡</span>
							<div class="bottom clearfix">
								<time class="time">{{ currentDate }}</time>
								<el-button type="text" class="button">操作按钮</el-button>
							</div>
						</div>
					</el-card>
				</el-col>
			</el-row>
		</div>


	</div>

</template>

<script>
export default{
	data(){
		return{
			ShowHouse:[
				{
					id:"100001",
					name:'望京新城',
					detail:'望京新城 三室一厅 东南',
					area:'96.47平米',
					price: '650万'
					
				},
				{
					id:"100002",
					name:'望京新城',
					detail:'望京新城 三室一厅 东南',
					area:'96.47平米',
					price: '650万'
				},
				{
					id:"100003",
					name:'望京新城',
					detail:'望京新城 三室一厅 东南',
					area:'96.47平米',
					price: '650万'
				},
				{
					id:"100004",
					name:'望京新城',
					detail:'望京新城 三室一厅 东南',
					area:'96.47平米',
					price: '650万'
				}
				
				
				]
		}
	}
}

</script>

<style>
	.time {
    font-size: 13px;
    color: #999;
  }
  
  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
	height: 120px;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  
  .clearfix:after {
      clear: both
  }
</style>
