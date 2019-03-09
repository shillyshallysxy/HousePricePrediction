<template>
	<div style="width: 100%;height: 100%;padding-left: 0px;">
		<div style="background-color: lightgray;width: 100%;max-height: 200px;padding-top:100px;padding-left: 0px;">
			<div style="width: 300px;height: 100px;margin-left: 150px;text-align: left;padding: 0px;">			
				<div style="background: #AAAAAA;max-height: 120px;max-width: 120px;border-radius:8px;float: left;">
					<img src="../assets/user.png" style="max-height: 120px;max-width: 120px;"/>
				</div>
				<p style="font-size: 15px;font-weight: 300;max-height: 20px;margin-top: 0;margin-left: 150px;">Username</p>
				<p style="font-size: 15px;font-weight: 300;max-height: 20px;margin-top:0;margin-left: 150px;">12345678@qq.com</p>
				<el-button size="small" round style="margin-top: 3px;margin-left: 20px;">编辑个人资料</el-button>
			</div>
		</div>
		
		<div style="width: 100%;padding: 0px;border-right: 0px;padding-left: 5%;">
			<div style="margin-left: 15%;margin-top: 50px;min-height: 30px;min-width: 80%;">
				<p style="font-size: 25px;float: left;"><b>我的收藏</b></p>
			</div>
			<div style="margin-left: 15%;height: 3px;width: 30%;background:black;overflow:hidden;margin-top: 40px;"></div>
			
			<ul style="width: 100%;position: relative;overflow: hidden;">
				<li v-bind:class="{collect:true}">
					<img src="../assets/login_back.jpg" style="max-height: 145px;max-width: 200px;min-height: 145px;min-width: 200px;background-size: 100% 100%;display: inline-block;"/>
					<div style="min-width: 500px;display: inline-block;padding: 0;position: absolute;top: 0px;left: 210px;">
						<p style="font-size: 18px;font-weight: 500;">
							满五年唯一 正规一居室可改二居 正对小区里头 安静
						</p>
						<p style="font-size: 12px;font-weight: 300;margin-left: 10px; max-width: 400px;">
							2室2厅，100平米，高楼层
							朝廷公寓，塔楼/板楼，楼龄
							北京正鹏房地产开发有限公司
						</p>
						<p style="font-size: 12px;font-weight: 300;margin-left: 10px;">
							取消收藏
						</p>
					</div>
					<div style="min-height: 150px;min-width: 200px;display: inline-block;padding: 0;position: absolute;top: 0px;left: 720px;">
						<p v-bind:class="{textColor:true}">
							540万
						</p>
						<p style="font-size: 12px;font-weight: 300;">
							单价：54000万
						</p>
						<p style="font-size: 12px;font-weight: 300;margin-top: 20px;">
							29人已收藏
						</p>
					</div>
					<div style="height: 1px;width: 80%;background:lightgrey;overflow:hidden;margin-top: 10px;"></div>
				</li>			
				<li v-bind:class="{collect:true}">
					<img src="../assets/2.jpg" style="max-height: 145px;max-width: 200px;min-height: 145px;min-width: 200px;background-size: 100% 100%;display: inline-block;"/>
					<div style="min-width: 500px;display: inline-block;padding: 0;position: absolute;top: 0px;left: 210px;">
						<p style="font-size: 18px;font-weight: 500;">
							满五年唯一 正规一居室可改二居 正对小区里头 安静
						</p>
						<p style="font-size: 12px;font-weight: 300;margin-left: 10px; max-width: 400px;">
							2室2厅，100平米，高楼层
							朝廷公寓，塔楼/板楼，楼龄
							北京正鹏房地产开发有限公司
						</p>
						<p style="font-size: 12px;font-weight: 300;margin-left: 10px;">
							取消收藏
						</p>
					</div>
					<div style="min-height: 150px;min-width: 200px;display: inline-block;padding: 0;position: absolute;top: 0px;left: 720px;">
						<p v-bind:class="{textColor:true}">
							540万
						</p>
						<p style="font-size: 12px;font-weight: 300;">
							单价：54000万
						</p>
						<p style="font-size: 12px;font-weight: 300;margin-top: 20px;">
							29人已收藏
						</p>
					</div>
					<div style="height: 1px;width: 80%;background:lightgrey;overflow:hidden;margin-top: 10px;"></div>
				</li>			
				<li v-bind:class="{collect:true}">
					<img src="../assets/2.jpg" style="max-height: 145px;max-width: 200px;min-height: 145px;min-width: 200px;background-size: 100% 100%;display: inline-block;"/>
					<div style="min-width: 500px;display: inline-block;padding: 0;position: absolute;top: 0px;left: 210px;">
						<p style="font-size: 18px;font-weight: 500;">
							满五年唯一 正规一居室可改二居 正对小区里头 安静
						</p>
						<p style="font-size: 12px;font-weight: 300;margin-left: 10px; max-width: 400px;">
							2室2厅，100平米，高楼层
							朝廷公寓，塔楼/板楼，楼龄
							北京正鹏房地产开发有限公司
						</p>
						<p style="font-size: 12px;font-weight: 300;margin-left: 10px;">
							取消收藏
						</p>
					</div>
					<div style="min-height: 150px;min-width: 200px;display: inline-block;padding: 0;position: absolute;top: 0px;left: 720px;">
						<p v-bind:class="{textColor:true}">
							540万
						</p>
						<p style="font-size: 12px;font-weight: 300;">
							单价：54000万
						</p>
						<p style="font-size: 12px;font-weight: 300;margin-top: 20px;">
							29人已收藏
						</p>
					</div>
					<div style="height: 1px;width: 80%;background:lightgrey;overflow:hidden;margin-top: 10px;"></div>
				</li>			
				<li v-bind:class="{collect:true}">
					<img src="../assets/2.jpg" style="max-height: 145px;max-width: 200px;min-height: 145px;min-width: 200px;background-size: 100% 100%;display: inline-block;"/>
					<div style="min-width: 500px;display: inline-block;padding: 0;position: absolute;top: 0px;left: 210px;">
						<p style="font-size: 18px;font-weight: 500;">
							满五年唯一 正规一居室可改二居 正对小区里头 安静
						</p>
						<p style="font-size: 12px;font-weight: 300;margin-left: 10px; max-width: 400px;">
							2室2厅，100平米，高楼层
							朝廷公寓，塔楼/板楼，楼龄
							北京正鹏房地产开发有限公司
						</p>
						<p style="font-size: 12px;font-weight: 300;margin-left: 10px;">
							取消收藏
						</p>
					</div>
					<div style="min-height: 150px;min-width: 200px;display: inline-block;padding: 0;position: absolute;top: 0px;left: 720px;">
						<p v-bind:class="{textColor:true}">
							540万
						</p>
						<p style="font-size: 12px;font-weight: 300;">
							单价：54000万
						</p>
						<p style="font-size: 12px;font-weight: 300;margin-top: 20px;">
							29人已收藏
						</p>
					</div>
					<div style="height: 1px;width: 80%;background:lightgrey;overflow:hidden;margin-top: 10px;"></div>
				</li>			
				<li v-bind:class="{collect:true}">
					<img src="../assets/2.jpg" style="max-height: 145px;max-width: 200px;min-height: 145px;min-width: 200px;background-size: 100% 100%;display: inline-block;"/>
					<div style="min-width: 500px;display: inline-block;padding: 0;position: absolute;top: 0px;left: 210px;">
						<p style="font-size: 18px;font-weight: 500;">
							满五年唯一 正规一居室可改二居 正对小区里头 安静
						</p>
						<p style="font-size: 12px;font-weight: 300;margin-left: 10px; max-width: 400px;">
							2室2厅，100平米，高楼层
							朝廷公寓，塔楼/板楼，楼龄
							北京正鹏房地产开发有限公司
						</p>
						<p style="font-size: 12px;font-weight: 300;margin-left: 10px;">
							取消收藏
						</p>
					</div>
					<div style="min-height: 150px;min-width: 200px;display: inline-block;padding: 0;position: absolute;top: 0px;left: 720px;">
						<p v-bind:class="{textColor:true}">
							540万
						</p>
						<p style="font-size: 12px;font-weight: 300;">
							单价：54000万
						</p>
						<p style="font-size: 12px;font-weight: 300;margin-top: 20px;">
							29人已收藏
						</p>
					</div>
					<div style="height: 1px;width: 80%;background:lightgrey;overflow:hidden;margin-top: 10px;"></div>
				</li>			
				
			</ul>
		
			<ul style="width: 100%;position: relative;margin-top: 30px;">
				<li v-bind:class="{item:true}">
					<a>1</a>
				</li>
				<li v-bind:class="{item:true}">
					<a>2</a>
				</li>
				<li v-bind:class="{item:true}">
					<a>3</a>
				</li>
			</ul>
		</div>
	</div>
</template>

<script>
</script>

<style>
.item{
	display: inline-block;
    vertical-align: middle;
    min-width: 32px;
    height: 32px;
    line-height: 30px;
    margin-right: 4px;
    text-align: center;
    list-style: none;
    background-color: #fff;
    user-select: none;
    cursor: pointer;
    font-family: Arial;
    font-weight: 500;
    border: 1px solid #dcdee2;
    border-radius: 4px;
    transition: border .2s ease-in-out,color .2s ease-in-out;
}
.item a{
	font-family: Monospaced Number;
    margin: 0 6px;
    text-decoration: none;
    color: #515a6e;
}
.collect{
	min-height: 150px;
	min-width: 1000px;
	max-height: 150px;
	margin-left: 15%;
	float: left;
	text-align: left;
	padding-top: 0;
	position: relative;
	margin-top: 20px;
	list-style: none;
}

.textColor{
	font-size: 28px;
	font-weight: 400;
	margin-top: 10px;
	color: rgb(252,124,0);
}
</style>
