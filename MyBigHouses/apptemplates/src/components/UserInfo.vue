<template>
	<div style="width: 100%;height: 100%;padding-left: 0px;">
		<div style="background-color: lightgray;width: 100%;max-height: 200px;padding-top:100px;padding-left: 0px;">
			<div style="width: 300px;height: 100px;margin-left: 150px;text-align: left;padding: 0px;">
				<!-- <div style="background: #AAAAAA;max-height: 120px;max-width: 120px;border-radius:8px;float: left;"> -->
				<el-upload class="avatar-uploader" name="file" :action="post_img_url" :headers="import_headers" :show-file-list="false"
				 :on-success="handleAvatarSuccess" :before-upload="beforeAvatarUpload">
					<img v-if="imageUrl" :src="imageUrl" class="avatar">
					<i v-else class="el-icon-plus avatar-uploader-icon"></i>
				</el-upload>
				<!-- <img src="../assets/user.png" style="max-height: 120px;max-width: 120px;"/> -->
				<!-- </div> -->
				<p style="font-size: 15px;font-weight: 300;max-height: 20px;margin-top: 0;margin-left: 150px;">{{user_name}}</p>
				<!-- <p style="font-size: 15px;font-weight: 300;max-height: 20px;margin-top:0;margin-left: 150px;">12345678@qq.com</p> -->
				<!-- <el-button size="small" round style="margin-top: 3px;margin-left: 20px;">编辑个人资料</el-button> -->
			</div>
		</div>
		<div class="body">
			<div class="list_content">
				<div style="margin-top: 50px;min-height: 30px;min-width: 80%;">
					<p style="font-size: 25px;float: left;"><b>我的收藏</b></p>
				</div>
				<div class="line"></div>

				<ul class="list">
					<li class="collect" v-for="(o, index) in favor_info" key='o.id'>
						<img :src="o.img_url" class="item_img" />

						<div class="block">
							<p style="font-size: 18px;font-weight: 500;cursor: pointer;" @click="go_to_detail(o.id)">
								{{o.description}}
							</p>
							<p class="desCollect">
								{{o.layout}}，{{o.area}}平米，{{o.layer}}
								{{o.garden}}，{{o.architecture}}，{{o.built_year}}
								{{o.developer}}
							</p>
							<div class="cancelCollect">
								<p style="font-size: 12px;font-weight: 300;margin-left: 10px; cursor: pointer;" @click="cancel_favour(o.id)">
									取消收藏
								</p>
							</div>

						</div>
						<div class="item_right">
							<p class="textColor">
								{{o.total_price}}万
							</p>
							<p style="font-size: 12px;font-weight: 300;">
								单价：{{o.price}}万
							</p>
							<p style="font-size: 12px;font-weight: 300;margin-top: 20px;">
								{{o.star_count}}人已收藏
							</p>
						</div>
						<div class="line1"></div>
					</li>
				</ul>

				<v-pagination :total="total" :current-page='current' @pagechange="pagechange"></v-pagination>


			</div>

		</div>

	</div>
</template>

<script>
	import store from '@/store'
	import global_ from '@/components/Global'
	import pagination from '@/components/MyPagenation'
	import {
		getCookie,
		setCookie,
		delCookie
	} from '@/utils/utils'
	export default {
		components: {
			'v-pagination': pagination,
		},
		data() {
			return {
				post_img_url: global_.IpUrl + '/user/modify_avatar',
				imageUrl: '',
				user_name: store.state.UserInfo.username,
				import_headers: {
					// 'Content-Type': 'multipart/form-data',
					'X-CSRFToken': getCookie('csrftoken')
				},
				favor_info: [],
				//分页实现内容
				total: 0, // 记录总条数
				display: 5, // 每页显示条数
				current: 1, // 当前的页数
			};

		},
		created() {
			this.getAvatar()
		},
		mounted() {
			this.getList()
		},
		methods: {
			getList() {
				this.favor_info = []
				console.log(this.current)
				let url = global_.IpUrl + '/user/get_info/?pag_num=' + this.current
				this.$ajax({
					url: url,
					method: 'get',
				}).then(function(response) {
					if (response.data.code === 0) {
						var favor = response.data.data
						for (var i = 0; i < favor.length; i++) {
							var temp = {}
							temp["description"] = favor[i].description
							temp["layout"] = favor[i].layout
							temp["layer"] = favor[i].layer
							temp["built_year"] = favor[i].built_year
							temp["area"] = favor[i].area
							temp["price"] = favor[i].price
							temp["total_price"] = favor[i].total_price
							temp["orientation"] = favor[i].orientation
							temp["garden"] = favor[i].garden
							temp["developer"] = favor[i].developer
							temp["architecture"] = favor[i].architecture
							temp["id"] = favor[i].id
							temp["img_url"] = favor[i].img_url
							temp["star_count"] = favor[i].star_count
							this.favor_info.push(temp)
							console.log(response.data.total_item_num)
							this.total = response.data.total_item_num
							
						}
					} else {
						iView.Message.info(response.data.msg)
					}
				}.bind(this))

			},
			pagechange(page) {
				this.current = page
				this.getList()
			},
			getAvatar() {
				this.$ajax({
					method: 'get',
					async: false,
					url: global_.IpUrl + '/user/get_info',
				}).then(function(response) {
					if (response.data.code == 0) {
						this.imageUrl = global_.IpUrl + '/' + response.data.img_url
					} else {
						iView.Message.info(response.data.msg)
					}
				}.bind(this))
			},
			handleAvatarSuccess(response, file) {
				if (response.code == 0) {
					// this.imageUrl = URL.createObjectURL(file.raw);
					this.imageUrl = global_.IpUrl + '/' + response.img_url
				} else {
					iView.Message.info(response.msg)
				}
			},
			beforeAvatarUpload(file) {
				const isJPG = file.type === 'image/jpeg';
				const isLt2M = file.size / 1024 / 1024 < 2;

				if (!isJPG) {
					this.$message.error('上传头像图片只能是 JPG 格式!');
				}
				if (!isLt2M) {
					this.$message.error('上传头像图片大小不能超过 2MB!');
				}
				return isJPG && isLt2M;
			},
			cancel_favour(id){
				console.log(id)
			},
			go_to_detail(id){
				this.$router.push({
					path: 'ItemPage',
					query: {
						HouseId: id
					}
				})
			}

		}
	}
</script>

<style scoped>
	.pageNumber {
		width: 950px;
		position: relative;
		margin-top: 30px;
	}

	.line {
		height: 3px;
		width: 30%;
		background: black;
		overflow: hidden;
		margin-top: 40px;
	}

	.line1 {
		height: 1px;
		width: 90%;
		background: lightgrey;
		overflow: hidden;
		margin-top: 10px
	}

	.body {
		width: 100%;
		height: 1000px;
		padding-left: 50%;
		margin-top: 40px;
	}

	.item {
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
		transition: border .2s ease-in-out, color .2s ease-in-out;
	}

	.item a {
		font-family: Monospaced Number;
		margin: 0 6px;
		text-decoration: none;
		color: #515a6e;
	}

	.collect {
		min-height: 150px;
		width: 950px;
		max-height: 150px;
		float: left;
		text-align: left;
		padding-top: 0;
		position: relative;
		margin-top: 20px;
		list-style: none;
	}

	.textColor {
		font-size: 28px;
		font-weight: 400;
		margin-top: 10px;
		color: rgb(252, 124, 0);
	}

	.avatar-uploader .el-upload {
		border: 1px dashed #d9d9d9;
		border-radius: 6px;
		cursor: pointer;
		position: relative;
		overflow: hidden;
	}

	.avatar-uploader .el-upload:hover {
		border-color: #409EFF;
	}

	.avatar-uploader-icon {
		font-size: 28px;
		color: #8c939d;
		width: 178px;
		height: 178px;
		line-height: 178px;
		text-align: center;
	}

	.avatar {
		width: 178px;
		height: 178px;
		display: block;
	}

	.list_content {
		width: 950px;
		height: 950px;
		margin-left: -475px;
		padding-top: 30px;
	}

	.list {
		width: 100%;
		position: relative;
		overflow: hidden;
	}

	.item_img {
		max-height: 145px;
		max-width: 200px;
		min-height: 145px;
		min-width: 200px;
		background-size: 100% 100%;
		display: inline-block;
	}

	.desCollect {
		font-size: 12px;
		font-weight: 300;
		margin-left: 10px;
		height: 80px;
		width: 400px;
	}

	.cancelCollect {
		width: 100px;
		margin-top: 20px;
		height: 20px;
	}

	.block {
		width: 500px;
		height: 150px;
		display: inline-block;
		padding: 0;
		position: absolute;
		top: 0px;
		left: 210px;
	}

	.item_right {
		height: 150px;
		width: 150px;
		display: inline-block;
		padding: 0;
		position: absolute;
		top: 0px;
		left: 800px;
	}
</style>
