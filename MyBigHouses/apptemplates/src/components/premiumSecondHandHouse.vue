<template>
    <div v-bind:class="{ershou: true}">
		<div v-bind:class="{search:true}">
			<el-row>
				<el-col :span="4"><div class="grid-content bg-purple"></div></el-col>
				<el-col :span="4"><div class="grid-content bg-purple-light"></div></el-col>
				<el-col :span="4"><div class="grid-content bg-purple"></div></el-col>
				<el-col :span="4"><div class="grid-content bg-purple-light"></div></el-col>
				<el-col :span="4"><div class="grid-content bg-purple"></div></el-col>
				<el-col :span="4"><div class="grid-content bg-purple-light"></div></el-col>
				<!--
				<el-col :span="1"><div class="grid-content bg-purple-dark"></div></el-col>
				精品二手房
				<el-input placeholder="您的心理价位"></el-input>
				<el-input placeholder="您的理想房屋面积"></el-input>
				<el-button>推荐</el-button>
				<p style="float:right;font-size: 5px;margin-right: 50px;">查看更多</p>
				-->
			</el-row>
		</div>
    </div>
</template>

<script>
export default {
    data() {

    },
    methods: {

    }
}
</script>

<style>
.el-input{
  width: 200px;
}
.el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
.el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
.ershou{
  height:200px;
  width:100%;
  padding:0px;
  margin:0px;
  background-color: red;
  display:block;
  position:relative;
  background-position-y: 0px
}
.search{
	height: 50px;
	width:100%;
	padding:0px;
	margin:0px;
	background-color: white;
	display:block;
	position:relative;
}

</style>
