<template>
	<div class="main-content" :style='{"color":"#666","padding":"20px 30px 30px","fontSize":"14px"}'>
		<!-- 列表页 -->
		<template v-if="showFlag">
			<el-form class="center-form-pv" :style='{"margin":"0 0 0px","fontSize":"inherit","flexWrap":"wrap","display":"flex"}' :inline="true" :model="searchForm">
				<el-row :style='{"margin":"0 50px 10px 0","fontSize":"inherit","display":"block"}' >
					<div :style='{"margin":"0 10px 0 0","fontSize":"inherit","display":"inline-block"}'>
						<label :style='{"margin":"0 10px 0 0","color":"inherit","display":"inline-block","lineHeight":"40px","fontSize":"inherit","fontWeight":"500","height":"40px"}' class="item-label">品牌</label>
						<el-input v-model="searchForm.pinpai" placeholder="品牌" @keydown.enter.native="search()" clearable></el-input>
					</div>
					<div :style='{"margin":"0 10px 0 0","fontSize":"inherit","display":"inline-block"}'>
						<label :style='{"margin":"0 10px 0 0","color":"inherit","display":"inline-block","lineHeight":"40px","fontSize":"inherit","fontWeight":"500","height":"40px"}' class="item-label">运行内存</label>
						<el-input v-model="searchForm.yxnc" placeholder="运行内存" @keydown.enter.native="search()" clearable></el-input>
					</div>
					<div :style='{"margin":"0 10px 0 0","fontSize":"inherit","display":"inline-block"}'>
						<label :style='{"margin":"0 10px 0 0","color":"inherit","display":"inline-block","lineHeight":"40px","fontSize":"inherit","fontWeight":"500","height":"40px"}' class="item-label">机身颜色</label>
						<el-input v-model="searchForm.jsys" placeholder="机身颜色" @keydown.enter.native="search()" clearable></el-input>
					</div>
					<div :style='{"margin":"0 10px 0 0","fontSize":"inherit","display":"inline-block"}'>
						<label :style='{"margin":"0 10px 0 0","color":"inherit","display":"inline-block","lineHeight":"40px","fontSize":"inherit","fontWeight":"500","height":"40px"}' class="item-label">机身内存</label>
						<el-input v-model="searchForm.jsnc" placeholder="机身内存" @keydown.enter.native="search()" clearable></el-input>
					</div>
					<el-button class="search" type="success" @click="search()">
						<span class="icon iconfont icon-yanziwancheng" :style='{"margin":"0 2px","fontSize":"inherit","color":"#fff","height":"40px"}'></span>
						搜索
					</el-button>
				</el-row>

				<el-row class="actions" :style='{"flexWrap":"wrap","margin":"0 0 10px","display":"flex"}'>
					<el-button class="add" v-if="isAuth('shouji','新增')" type="success" @click="addOrUpdateHandler()">
						<span class="icon iconfont icon-kaitongfuwu" :style='{"margin":"0 2px","fontSize":"inherit","color":"#fff","height":"40px"}'></span>
						新增
					</el-button>
					<el-button class="del" v-if="isAuth('shouji','删除')" :disabled="dataListSelections.length?false:true" type="danger" @click="deleteHandler()">
						<span class="icon iconfont icon-guanbi1" :style='{"margin":"0 2px","fontSize":"inherit","color":"#fff","height":"40px"}'></span>
						删除
					</el-button>


					<el-button class="btn18" v-if="isAuth('shouji','爬取数据')" type="success" @click="spider()">
						<span class="icon iconfont icon-fenxiang" :style='{"margin":"0 2px","fontSize":"inherit","color":"#fff","height":"40px"}'></span>
						爬取数据
					</el-button>
					<el-button class="btn18" v-if="isAuth('shouji','生成数据')" type="success" @click="genDataClick()">
						<span class="icon iconfont icon-fenxiang" :style='{"margin":"0 2px","fontSize":"inherit","color":"#fff","height":"40px"}'></span>
						生成数据
					</el-button>

					<el-button class="btn18" v-if="isAuth('shouji','品牌统计')" type="success" @click="chartDialog1()">
						<span class="icon iconfont icon-xihuan" :style='{"margin":"0 2px","fontSize":"inherit","color":"#fff","height":"40px"}'></span>
						品牌统计
					</el-button>
					<el-button class="btn18" v-if="isAuth('shouji','运行内存')" type="success" @click="chartDialog2()">
						<span class="icon iconfont icon-xihuan" :style='{"margin":"0 2px","fontSize":"inherit","color":"#fff","height":"40px"}'></span>
						运行内存
					</el-button>
					<el-button class="btn18" v-if="isAuth('shouji','评论数')" type="success" @click="chartDialog3()">
						<span class="icon iconfont icon-xihuan" :style='{"margin":"0 2px","fontSize":"inherit","color":"#fff","height":"40px"}'></span>
						评论数
					</el-button>
					<el-button class="btn18" v-if="isAuth('shouji','机身颜色')" type="success" @click="chartDialog4()">
						<span class="icon iconfont icon-xihuan" :style='{"margin":"0 2px","fontSize":"inherit","color":"#fff","height":"40px"}'></span>
						机身颜色
					</el-button>
					<el-button class="btn18" v-if="isAuth('shouji','机身内存')" type="success" @click="chartDialog5()">
						<span class="icon iconfont icon-xihuan" :style='{"margin":"0 2px","fontSize":"inherit","color":"#fff","height":"40px"}'></span>
						机身内存
					</el-button>
				</el-row>
			</el-form>
			<div :style='{"width":"100%","padding":"0","background":"none"}'>
				<el-table class="tables"
					:stripe='false'
					:style='{"padding":"0","borderColor":"#eee","color":"inherit","borderWidth":"1px 0 0 1px","background":"#fff","width":"100%","fontSize":"inherit","borderStyle":"solid"}' 
					:border='true'
					v-if="isAuth('shouji','查看')"
					:data="dataList"
					v-loading="dataListLoading"
				@selection-change="selectionChangeHandler">
					<el-table-column :resizable='true' type="selection" align="center" width="50"></el-table-column>
					<el-table-column :resizable='true' :sortable='true' label="序号" type="index" width="50" />
					<!-- biaoti -->
					<!-- 1,5 -->
					<el-table-column :resizable='true' :sortable='true'  
						prop="biaoti"
						label="标题">
						<template slot-scope="scope">
							{{scope.row.biaoti}}
						</template>
					</el-table-column>
					<!-- laiyuan -->
					<!-- $column.hiden -->
					<!-- fengmian -->
					<!-- $column.hiden -->
					<!-- 无 -->
					<el-table-column :resizable='true' :sortable='true' prop="fengmian" width="200" label="封面">
						<template slot-scope="scope">
							<div v-if="scope.row.fengmian">
								<img v-if="scope.row.fengmian.substring(0,4)=='http'" :src="scope.row.fengmian.split(',')[0]" width="100" height="100" style="object-fit: cover">
								<img v-else :src="$base.url+scope.row.fengmian.split(',')[0]" width="100" height="100" style="object-fit: cover">
							</div>
							<div v-else>无图片</div>
						</template>
					</el-table-column>
					<!-- jiage -->
					<!-- $column.hiden -->
					<el-table-column :resizable='true' :sortable='true'  
						prop="jiage"
						label="价格">
						<template slot-scope="scope">
							{{scope.row.jiage}}
						</template>
					</el-table-column>
					<!-- pinpai -->
					<!-- 5 -->
					<el-table-column :resizable='true' :sortable='true'  
						prop="pinpai"
						label="品牌">
						<template slot-scope="scope">
							{{scope.row.pinpai}}
						</template>
					</el-table-column>
					<!-- spcd -->
					<!-- $column.hiden -->
					<!-- yxnc -->
					<!-- 5 -->
					<el-table-column :resizable='true' :sortable='true'  
						prop="yxnc"
						label="运行内存">
						<template slot-scope="scope">
							{{scope.row.yxnc}}
						</template>
					</el-table-column>
					<!-- jsys -->
					<!-- 5 -->
					<el-table-column :resizable='true' :sortable='true'  
						prop="jsys"
						label="机身颜色">
						<template slot-scope="scope">
							{{scope.row.jsys}}
						</template>
					</el-table-column>
					<!-- jsnc -->
					<!-- 5 -->
					<el-table-column :resizable='true' :sortable='true'  
						prop="jsnc"
						label="机身内存">
						<template slot-scope="scope">
							{{scope.row.jsnc}}
						</template>
					</el-table-column>
					<!-- hszxs -->
					<!-- 5 -->
					<el-table-column :resizable='true' :sortable='true'  
						prop="hszxs"
						label="后摄主像素">
						<template slot-scope="scope">
							{{scope.row.hszxs}}
						</template>
					</el-table-column>
					<!-- fengge -->
					<!-- 5 -->
					<el-table-column :resizable='true' :sortable='true'  
						prop="fengge"
						label="风格">
						<template slot-scope="scope">
							{{scope.row.fengge}}
						</template>
					</el-table-column>
					<!-- xiaoliang -->
					<!-- 5 -->
					<el-table-column :resizable='true' :sortable='true'  
						prop="xiaoliang"
						label="评论数">
						<template slot-scope="scope">
							{{scope.row.xiaoliang}}
						</template>
					</el-table-column>
					<!-- comment -->
					<!-- $column.hiden -->
					<el-table-column width="300" label="操作">
						<template slot-scope="scope">
							<el-button class="view" v-if=" isAuth('shouji','查看')" type="success" @click="addOrUpdateHandler(scope.row.id,'info')">
								<span class="icon iconfont icon-dagou" :style='{"margin":"0 2px","fontSize":"inherit","color":"inherit","height":"40px"}'></span>
								查看
							</el-button>
							<el-button class="edit" v-if=" isAuth('shouji','修改') " type="success" @click="addOrUpdateHandler(scope.row.id)">
								<span class="icon iconfont icon-bianji" :style='{"margin":"0 2px","fontSize":"inherit","color":"inherit","height":"40px"}'></span>
								修改
							</el-button>




							<el-button class="del" v-if="isAuth('shouji','删除') " type="primary" @click="deleteHandler(scope.row.id )">
								<span class="icon iconfont icon-guanbi1" :style='{"margin":"0 2px","fontSize":"inherit","color":"inherit","height":"40px"}'></span>
								删除
							</el-button>
						</template>
					</el-table-column>
				</el-table>
			</div>
			<el-pagination
				@size-change="sizeChangeHandle"
				@current-change="currentChangeHandle"
				:current-page="pageIndex"
				background
				:page-sizes="[10, 50, 100, 200]"
				:page-size="pageSize"
				:layout="layouts.join()"
				:total="totalPage"
				prev-text="上一页 "
				next-text="下一页 "
				:hide-on-single-page="false"
				:style='{"padding":"0","margin":"20px 0 0","whiteSpace":"nowrap","color":"inherit","width":"100%","fontSize":"inherit","fontWeight":"500"}'
			></el-pagination>
		</template>
		
		<!-- 添加/修改页面  将父组件的search方法传递给子组件-->
		<add-or-update v-if="addOrUpdateFlag" :parent="this" ref="addOrUpdate"></add-or-update>





		<el-dialog
		  :visible.sync="chartVisiable1"
		  width="800">
			<div id="pinpaiChart1" style="width:100%;height:600px;"></div>
		  <span slot="footer" class="dialog-footer">
			<el-button @click="chartDialog1">返回</el-button>
		  </span>
		</el-dialog>
		<el-dialog
		  :visible.sync="chartVisiable2"
		  width="800">
			<div id="yxncChart2" style="width:100%;height:600px;"></div>
		  <span slot="footer" class="dialog-footer">
			<el-button @click="chartDialog2">返回</el-button>
		  </span>
		</el-dialog>
		<el-dialog
		  :visible.sync="chartVisiable3"
		  width="800">
			<div id="xiaoliangChart3" style="width:100%;height:600px;"></div>
		  <span slot="footer" class="dialog-footer">
			<el-button @click="chartDialog3">返回</el-button>
		  </span>
		</el-dialog>
		<el-dialog
		  :visible.sync="chartVisiable4"
		  width="800">
			<div id="jsysChart4" style="width:100%;height:600px;"></div>
		  <span slot="footer" class="dialog-footer">
			<el-button @click="chartDialog4">返回</el-button>
		  </span>
		</el-dialog>
		<el-dialog
		  :visible.sync="chartVisiable5"
		  width="800">
			<div id="jsncChart5" style="width:100%;height:600px;"></div>
		  <span slot="footer" class="dialog-footer">
			<el-button @click="chartDialog5">返回</el-button>
		  </span>
		</el-dialog>
		<el-dialog :title="'生成数据'" :visible.sync="genDataVisible" width="50%">
			<el-form ref="form" :model="genDataForm" label-width="100px">
				<el-form-item label="数据量">
					<el-input-number v-model="genDataForm.recordNum" :min="1" :max="1000" label="数据量"></el-input-number>
				</el-form-item>
			</el-form>
			<span slot="footer" class="dialog-footer">
				<el-button @click="genDataVisible = false">关闭</el-button>
				<el-button @click="genDataSave" type="primary">生成</el-button>
			</span>
		</el-dialog>
	</div>
</template>

<script>
import * as echarts from 'echarts'
import chinaJson from "@/components/echarts/china.json";
import axios from 'axios'
import AddOrUpdate from "./add-or-update";
import {
  Loading
} from 'element-ui'
	export default {
		data() {
			return {
				searchForm: {
					key: ""
				},
				form:{},
				dataList: [],
				pageIndex: 1,
				pageSize: 10,
				totalPage: 0,
				dataListLoading: false,
				dataListSelections: [],
				showFlag: true,
				sfshVisiable: false,
				shForm: {},
				chartVisiable: false,
				chartVisiable1: false,
				chartVisiable2: false,
				chartVisiable3: false,
				chartVisiable4: false,
				chartVisiable5: false,
				addOrUpdateFlag:false,
				layouts: ["total","prev","pager","next","sizes","jumper"],
				genDataVisible: false,
				genDataForm: {},
			};
		},
		created() {
			this.init();
			this.getDataList();
			this.contentStyleChange()
		},
		mounted() {
		},
		filters: {
			htmlfilter: function (val) {
				return val.replace(/<[^>]*>/g).replace(/undefined/g,'');
			}
		},
		computed: {
			tablename(){
				return this.$storage.get('sessionTable')
			},
		},
		components: {
			AddOrUpdate,
		},
		methods: {
			contentStyleChange() {
				this.contentPageStyleChange()
			},
			// 分页
			contentPageStyleChange(){
				let arr = []

				// if(this.contents.pageTotal) arr.push('total')
				// if(this.contents.pageSizes) arr.push('sizes')
				// if(this.contents.pagePrevNext){
				//   arr.push('prev')
				//   if(this.contents.pagePager) arr.push('pager')
				//   arr.push('next')
				// }
				// if(this.contents.pageJumper) arr.push('jumper')
				// this.layouts = arr.join()
				// this.contents.pageEachNum = 10
			},


//统计接口
    chartDialog1() {
      this.chartVisiable1 = !this.chartVisiable1;
      this.$nextTick(()=>{
        var pinpaiChart1 = echarts.init(document.getElementById("pinpaiChart1"),'macarons');
        this.$http({
            url: "shouji/group/pinpai",
            method: "get",
        }).then(({ data }) => {
            if (data && data.code === 0) {
                let res = data.data;
                let xAxis = [];
                let yAxis = [];
                let pArray = []
                for(let i=0;i<res.length;i++){
                    xAxis.push(res[i].pinpai);
                    yAxis.push(parseFloat((res[i].total)));
                    pArray.push({
                        value: parseFloat((res[i].total)),
                        name: res[i].pinpai
                    })
                }
                var option = {};
                option = {
                        title: {
                            text: '品牌统计',
                            left: 'center'
                        },
                        legend: {
                          orient: 'vertical',
                          left: 'left'
                        },
                        tooltip: {
                          trigger: 'item',
                          formatter: '{b} : {c} ({d}%)'
                        },
                        series: [
                            {
                                type: 'pie',
                                radius: '55%',
                                center: ['50%', '60%'],
                                data: pArray,
                                emphasis: {
                                    itemStyle: {
                                        shadowBlur: 10,
                                        shadowOffsetX: 0,
                                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                                    }
                                }
                            }
                        ]
                };
                // 使用刚指定的配置项和数据显示图表。
                pinpaiChart1.setOption(option);
                  //根据窗口的大小变动图表
                window.onresize = function() {
                    pinpaiChart1.resize();
                };
            }
        });
      })
    },

//统计接口
    chartDialog2() {
      this.chartVisiable2 = !this.chartVisiable2;
      this.$nextTick(()=>{

        var yxncChart2 = echarts.init(document.getElementById("yxncChart2"),'macarons');
        this.$http({
            url: "shouji/group/yxnc",
            method: "get",
        }).then(({ data }) => {
            if (data && data.code === 0) {
                let res = data.data;
                let xAxis = [];
                let yAxis = [];
                let pArray = []
                for(let i=0;i<res.length;i++){
                    xAxis.push(res[i].yxnc);
                    yAxis.push(parseFloat((res[i].total)));
                    pArray.push({
                        value: parseFloat((res[i].total)),
                        name: res[i].yxnc
                    })
                }
                var option = {};
                option = {
                    title: {
                        text: '运行内存',
                        left: 'center'
                    },
                    tooltip: {
                      trigger: 'item',
                      formatter: '{b} : {c}'
                    },
                    xAxis: {
                        type: 'category',
                        data: xAxis,
                        axisLabel : {
                            rotate:40
                        }
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [{
                        data: yAxis,
                        type: 'bar'
                    }]
                };
                // 使用刚指定的配置项和数据显示图表。
                yxncChart2.setOption(option);
                  //根据窗口的大小变动图表
                window.onresize = function() {
                    yxncChart2.resize();
                };
            }
        });
      })
    },

//统计接口
    chartDialog3() {
      this.chartVisiable3 = !this.chartVisiable3;
      this.$nextTick(()=>{
        // biaoti biaoti
        //  xiaoliang

        var xiaoliangChart3 = echarts.init(document.getElementById("xiaoliangChart3"),'macarons');
        this.$http({
            url: `shouji/value/biaoti/xiaoliang`,
            method: "get",
        }).then(({ data }) => {
            if (data && data.code === 0) {
                let res = data.data;
                let xAxis = [];
                let yAxis = [];
                let pArray = []
                for(let i=0;i<res.length;i++){
                    xAxis.push(res[i].biaoti);
                    yAxis.push(parseFloat((res[i].total)));
                    pArray.push({
                        value: parseFloat((res[i].total)),
                        name: res[i].biaoti
                    })
                }
                var option = {};
                option = {
                    title: {
                        text: '评论数',
                        left: 'center'
                    },
                    tooltip: {
                      trigger: 'item',
                      formatter: '{b} : {c}'
                    },
                    xAxis: {
                        type: 'category',
                        data: xAxis,
                        axisLabel : {
                            rotate:40
                        }
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [{
                        data: yAxis,
                        type: 'bar'
                    }]
                };
                // 使用刚指定的配置项和数据显示图表。
                xiaoliangChart3.setOption(option);
                  //根据窗口的大小变动图表
                window.onresize = function() {
                    xiaoliangChart3.resize();
                };
            }
        });
      })
    },

//统计接口
    chartDialog4() {
      this.chartVisiable4 = !this.chartVisiable4;
      this.$nextTick(()=>{

        var jsysChart4 = echarts.init(document.getElementById("jsysChart4"),'macarons');
        this.$http({
            url: "shouji/group/jsys",
            method: "get",
        }).then(({ data }) => {
            if (data && data.code === 0) {
                let res = data.data;
                let xAxis = [];
                let yAxis = [];
                let pArray = []
                for(let i=0;i<res.length;i++){
                    xAxis.push(res[i].jsys);
                    yAxis.push(parseFloat((res[i].total)));
                    pArray.push({
                        value: parseFloat((res[i].total)),
                        name: res[i].jsys
                    })
                }
                var option = {};
                option = {
                    title: {
                        text: '机身颜色',
                        left: 'center'
                    },
                    tooltip: {
                      trigger: 'item',
                      formatter: '{b} : {c}'
                    },
                    xAxis: {
                        type: 'value'
                    },
                    yAxis: {
                        type: 'category',
                        data: xAxis
                    },
                    series: [{
                        data: yAxis,
                        type: 'bar'
                    }]
                };
                // 使用刚指定的配置项和数据显示图表。
                jsysChart4.setOption(option);
                  //根据窗口的大小变动图表
                window.onresize = function() {
                    jsysChart4.resize();
                };
            }
        });
      })
    },

//统计接口
    chartDialog5() {
      this.chartVisiable5 = !this.chartVisiable5;
      this.$nextTick(()=>{

        var jsncChart5 = echarts.init(document.getElementById("jsncChart5"),'macarons');
        this.$http({
            url: "shouji/group/jsnc",
            method: "get",
        }).then(({ data }) => {
            if (data && data.code === 0) {
                let res = data.data;
                let xAxis = [];
                let yAxis = [];
                let pArray = []
                for(let i=0;i<res.length;i++){
                    xAxis.push(res[i].jsnc);
                    yAxis.push(parseFloat((res[i].total)));
                    pArray.push({
                        value: parseFloat((res[i].total)),
                        name: res[i].jsnc
                    })
                }
                var option = {};
                option = {
                    title: {
                        text: '机身内存',
                        left: 'center'
                    },
                    tooltip: {
                      trigger: 'item',
                      formatter: '{b} : {c}'
                    },
                    xAxis: {
                        type: 'category',
                        data: xAxis,
                        axisLabel : {
                            rotate:40
                        }
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [{
                        data: yAxis,
                        type: 'bar'
                    }]
                };
                // 使用刚指定的配置项和数据显示图表。
                jsncChart5.setOption(option);
                  //根据窗口的大小变动图表
                window.onresize = function() {
                    jsncChart5.resize();
                };
            }
        });
      })
    },
    init () {
    },
    search() {
      this.pageIndex = 1;
      this.getDataList();
    },

    // 获取数据列表
    getDataList() {
      this.dataListLoading = true;
      let params = {
        page: this.pageIndex,
        limit: this.pageSize,
        sort: 'id',
        order: 'desc',
      }
           if(this.searchForm.pinpai!='' && this.searchForm.pinpai!=undefined){
            params['pinpai'] = '%' + this.searchForm.pinpai + '%'
          }
           if(this.searchForm.yxnc!='' && this.searchForm.yxnc!=undefined){
            params['yxnc'] = '%' + this.searchForm.yxnc + '%'
          }
           if(this.searchForm.jsys!='' && this.searchForm.jsys!=undefined){
            params['jsys'] = '%' + this.searchForm.jsys + '%'
          }
           if(this.searchForm.jsnc!='' && this.searchForm.jsnc!=undefined){
            params['jsnc'] = '%' + this.searchForm.jsnc + '%'
          }
			this.$http({
				url: "shouji/page",
				method: "get",
				params: params
			}).then(({ data }) => {
				if (data && data.code === 0) {
					this.dataList = data.data.list;
					this.totalPage = data.data.total;
				} else {
					this.dataList = [];
					this.totalPage = 0;
				}
				this.dataListLoading = false;
			});
    },
    // 每页数
    sizeChangeHandle(val) {
      this.pageSize = val;
      this.pageIndex = 1;
      this.getDataList();
    },
    // 当前页
    currentChangeHandle(val) {
      this.pageIndex = val;
      this.getDataList();
    },
    // 多选
    selectionChangeHandler(val) {
      this.dataListSelections = val;
    },
    // 添加/修改
    addOrUpdateHandler(id,type) {
      this.showFlag = false;
      this.addOrUpdateFlag = true;
      this.crossAddOrUpdateFlag = false;
      if(type!='info'){
        type = 'else';
      }
      this.$nextTick(() => {
        this.$refs.addOrUpdate.init(id,type);
      });
    },
    // 下载
    download(file){
      let arr = file.replace(new RegExp('upload/', "g"), "")
      axios.get(this.$base.url + 'file/download?fileName=' + arr, {
      	headers: {
      		token: this.$storage.get('Token')
      	},
      	responseType: "blob"
      }).then(({
      	data
      }) => {
      	const binaryData = [];
      	binaryData.push(data);
      	const objectUrl = window.URL.createObjectURL(new Blob(binaryData, {
      		type: 'application/pdf;chartset=UTF-8'
      	}))
      	const a = document.createElement('a')
      	a.href = objectUrl
      	a.download = arr
      	// a.click()
      	// 下面这个写法兼容火狐
      	a.dispatchEvent(new MouseEvent('click', {
      		bubbles: true,
      		cancelable: true,
      		view: window
      	}))
      	window.URL.revokeObjectURL(data)
      },err=>{
		  axios.get((location.href.split(this.$base.name).length>1 ? location.href.split(this.$base.name)[0] :'') + this.$base.name + '/file/download?fileName=' + arr, {
		  	headers: {
		  		token: this.$storage.get('Token')
		  	},
		  	responseType: "blob"
		  }).then(({
		  	data
		  }) => {
		  	const binaryData = [];
		  	binaryData.push(data);
		  	const objectUrl = window.URL.createObjectURL(new Blob(binaryData, {
		  		type: 'application/pdf;chartset=UTF-8'
		  	}))
		  	const a = document.createElement('a')
		  	a.href = objectUrl
		  	a.download = arr
		  	// a.click()
		  	// 下面这个写法兼容火狐
		  	a.dispatchEvent(new MouseEvent('click', {
		  		bubbles: true,
		  		cancelable: true,
		  		view: window
		  	}))
		  	window.URL.revokeObjectURL(data)
		  })
	  })
    },
	// 预览
	preClick(file){
		if(!file){
			return false
		}
		window.open((location.href.split(this.$base.name).length>1 ? location.href.split(this.$base.name)[0] + this.$base.name + '/' + file :this.$base.url + file))
	},
	shoujistatusChange(e,row){
		if(row.status==0){
			row.passwordwrongnum = 0
		}
		this.$http({
			url:'shouji/update',
			method:'post',
			data:row
		}).then(res=>{
			if(row.status==1){
				this.$message.error('该用户已锁定')
			}else{
				this.$message.success('该用户已解除锁定')
			}
		})
	},
    // 删除
    deleteHandler(id ) {
      var ids = id
        ? [Number(id)]
        : this.dataListSelections.map(item => {
            return Number(item.id);
          });
      this.$confirm(`确定进行[${id ? "删除" : "批量删除"}]操作?`, "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning"
      }).then(() => {
        this.$http({
          url: "shouji/delete",
          method: "post",
          data: ids
        }).then(({ data }) => {
          if (data && data.code === 0) {
			this.$message({
			  message: "操作成功",
			  type: "success",
			  duration: 1500,
			  onClose: () => {
			    this.search();
			  }
			});
            
          } else {
            this.$message.error(data.msg);
          }
        });
      });
    },

    spider() {
        this.$message({
              message: "数据爬取中...",
              type: "success",
              duration: 3000,
              onClose: () => {
                this.search();
              }
            });
        this.$http({
          url: "spider/shouji",
          method: "get",
        }).then(({ data }) => {
          if (data && data.code === 0) {
            this.$message({
                message: "爬取完成",
                type: "success",
                duration: 1500,
                onClose: () => {
                    this.getDataList(this.roleName);
                }
            });
          } else {
            this.$alert(data.msg)
          }
        });
    },

	// 数据生成
	genDataClick(){
		this.genDataVisible = true
		this.genDataForm = {
			recordNum: 0
		}
	},
	genDataSave(){
		this.genDataVisible = false
        let loading = null
        loading = Loading.service({
			target: this.$refs['roleMenuBox'],
			fullscreen: false,
			text: '数据生成中...'
        })
		this.$http({
			url: 'shouji/batch/gen?recordNum=' + this.genDataForm.recordNum,
			method: 'post'
		}).then(res=>{
			if(res.data&&res.data.code==0){
				if (loading) loading.close()
				this.$message({
				    message: "数据生成成功！",
				    type: "success",
				    duration: 1500,
				    onClose: () => {
				        
				        this.getDataList()
				    }
				});
				
			}
		})
	},
  }

};
</script>
<style lang="scss" scoped>
	
	.center-form-pv {
	  .el-date-editor.el-input {
	    width: auto;
	  }
	}
	
	.el-input {
	  width: auto;
	}
	
	// form
	.center-form-pv .el-input /deep/ .el-input__inner {
				border: 0px solid #eee;
				border-radius: 0px;
				padding: 0 12px;
				box-shadow: 0 0 0px rgba(64, 158, 255, .5);
				outline: none;
				clip-path: polygon(95% 0, 100% 50%, 95% 99%, 0% 100%, 0% 0%);
				color: inherit;
				background: rgba(86,178,198,.2);
				width: 170px;
				font-size: inherit;
				height: 40px;
			}
	
	.center-form-pv .el-select /deep/ .el-input__inner {
				border: 0;
				border-radius: 0px;
				padding: 0 10px;
				box-shadow: 0 0 0px rgba(64, 158, 255, .5);
				outline: none;
				clip-path: polygon(95% 0, 100% 50%, 95% 99%, 0% 100%, 0% 0%);
				color: inherit;
				background: rgba(86,178,198,.2);
				width: 170px;
				font-size: inherit;
				height: 40px;
			}
	
	.center-form-pv .el-date-editor /deep/ .el-input__inner {
				border: 0;
				border-radius: 0px;
				padding: 0 10px 0 30px;
				box-shadow: 0 0 0px rgba(64, 158, 255, .5);
				outline: none;
				clip-path: polygon(95% 0, 100% 50%, 95% 99%, 0% 100%, 0% 0%);
				color: inherit;
				background: rgba(86,178,198,.2);
				width: 170px;
				font-size: inherit;
				height: 40px;
			}
	
	.center-form-pv .search {
				border: 0;
				cursor: pointer;
				border-radius: 0px;
				padding: 0 24px;
				outline: none;
				clip-path: polygon(95% 0, 100% 50%, 95% 100%, 0% 100%, 0 50%, 0% 0);
				color: #fff;
				background: rgba(86,178,198,.8);
				width: auto;
				font-size: inherit;
				height: 40px;
			}
	
	.center-form-pv .search:hover {
				opacity: 0.8;
			}
	
	.center-form-pv .actions .add {
				border: 0;
				cursor: pointer;
				border-radius: 0px;
				padding: 0 10px;
				margin: 0px 4px 10px;
				outline: none;
				clip-path: polygon(95% 0, 100% 50%, 95% 100%, 0% 100%, 0 50%, 0% 0);
				color: #fff;
				background: rgba(86,178,198,.8);
				width: auto;
				font-size: inherit;
				height: 40px;
			}
	
	.center-form-pv .actions .add:hover {
				opacity: 0.8;
			}
	
	.center-form-pv .actions .del {
				border: 0;
				cursor: pointer;
				border-radius: 0px;
				padding: 0 10px;
				margin: 0px 4px 10px;
				outline: none;
				clip-path: polygon(95% 0, 100% 50%, 95% 100%, 0% 100%, 0 50%, 0% 0);
				color: #fff;
				background: rgba(255, 0, 0, .8);
				width: auto;
				font-size: inherit;
				height: 40px;
			}
	
	.center-form-pv .actions .del:hover {
				opacity: 0.8;
			}
	
	.center-form-pv .actions .statis {
				border: 0;
				cursor: pointer;
				border-radius: 0px;
				padding: 0 10px;
				margin: 0px 4px 10px;
				outline: none;
				clip-path: polygon(95% 0, 100% 50%, 95% 100%, 0% 100%, 0 50%, 0% 0);
				color: #fff;
				background: rgba(255, 128, 0, 1);
				width: auto;
				font-size: inherit;
				height: 40px;
			}
	
	.center-form-pv .actions .statis:hover {
				opacity: 0.8;
			}
	
	.center-form-pv .actions .btn18 {
				border: 0;
				cursor: pointer;
				border-radius: 0px;
				padding: 0 10px;
				margin: 0px 4px 10px;
				outline: none;
				clip-path: polygon(95% 0, 100% 50%, 95% 100%, 0% 100%, 0 50%, 0% 0);
				color: #fff;
				background: rgba(255, 128, 0, 1);
				width: auto;
				font-size: inherit;
				height: 40px;
			}
	
	.center-form-pv .actions .btn18:hover {
				opacity: 0.8;
			}
	
	// table
	.el-table /deep/ .el-table__header-wrapper thead {
				clip-path: polygon(100% 0%, 100% 50%, 99% 100%, 1% 100%, 0% 50%, 0 0);
				color: #fff;
				background: rgba(86,178,198,.8);
				font-weight: 500;
				width: 100%;
			}
	
	.el-table /deep/ .el-table__header-wrapper thead tr {
				background: none;
			}
	
	.el-table /deep/ .el-table__header-wrapper thead tr th {
				padding: 12px 0;
				background: none;
				border-color: #eee;
				border-width: 0 1px 1px 0;
				border-style: solid;
				text-align: left;
			}

	.el-table /deep/ .el-table__header-wrapper thead tr th .cell {
				padding: 0 10px;
				word-wrap: normal;
				word-break: break-all;
				white-space: normal;
				font-weight: bold;
				display: inline-block;
				vertical-align: middle;
				width: 100%;
				line-height: 24px;
				position: relative;
				text-overflow: ellipsis;
			}

	
	.el-table /deep/ .el-table__body-wrapper tbody {
				width: 100%;
			}

	.el-table /deep/ .el-table__body-wrapper tbody tr {
				background: #fff;
			}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td {
				padding: 6px 0;
				color: inherit;
				background: #fff;
				font-size: inherit;
				border-color: #eee;
				border-width: 0 1px 1px 0;
				border-style: solid;
				text-align: left;
			}
	
		
	.el-table /deep/ .el-table__body-wrapper tbody tr:hover td {
				padding: 6px 0;
				color: #666;
				background: rgba(86,178,198,.05);
				border-color: #eee;
				border-width: 0 1px 1px 0;
				border-style: solid;
				text-align: left;
			}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td {
				padding: 6px 0;
				color: inherit;
				background: #fff;
				font-size: inherit;
				border-color: #eee;
				border-width: 0 1px 1px 0;
				border-style: solid;
				text-align: left;
			}

	.el-table /deep/ .el-table__body-wrapper tbody tr td .cell {
				padding: 0 10px;
				overflow: hidden;
				color: inherit;
				word-break: break-all;
				white-space: normal;
				line-height: 24px;
				text-overflow: ellipsis;
			}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .view {
				border: 0;
				cursor: pointer;
				border-radius: 0px;
				padding: 0 10px;
				margin: 0 5px 5px 0;
				outline: none;
				clip-path: polygon(0% 0%, 95% 0, 100% 50%, 95% 100%, 0% 100%);
				color: #fff;
				background: rgba(86,178,198,.8);
				width: auto;
				font-size: inherit;
				height: 32px;
			}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .view:hover {
				opacity: 0.8;
			}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .add {
			}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .add:hover {
			}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .edit {
				border: 0;
				cursor: pointer;
				border-radius: 0px;
				padding: 0 10px;
				margin: 0 5px 5px 0;
				outline: none;
				clip-path: polygon(0% 0%, 95% 0, 100% 50%, 95% 100%, 0% 100%);
				color: #fff;
				background: rgba(64, 158, 255, 1);
				width: auto;
				font-size: inherit;
				height: 32px;
			}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .edit:hover {
				opacity: 0.8;
			}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .del {
				border: 0;
				cursor: pointer;
				border-radius: 0px;
				padding: 0 10px;
				margin: 0 5px 5px 0;
				outline: none;
				clip-path: polygon(0% 0%, 95% 0, 100% 50%, 95% 100%, 0% 100%);
				color: #fff;
				background: rgba(255, 0, 0, 1);
				width: auto;
				font-size: inherit;
				height: 32px;
			}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .del:hover {
				opacity: 0.8;
			}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .btn8 {
				border: 0;
				cursor: pointer;
				border-radius: 0px;
				padding: 0 10px;
				margin: 0 5px 5px 0;
				outline: none;
				clip-path: polygon(0% 0%, 95% 0, 100% 50%, 95% 100%, 0% 100%);
				color: #fff;
				background: rgba(255, 128, 0, 1);
				width: auto;
				font-size: inherit;
				height: 32px;
			}
	
	.el-table /deep/ .el-table__body-wrapper tbody tr td .btn8:hover {
				opacity: 0.8;
			}
	
	// pagination
	.main-content .el-pagination /deep/ .el-pagination__total {
				margin: 0 10px 0 0;
				color: inherit;
				font-weight: 400;
				display: inline-block;
				vertical-align: top;
				font-size: inherit;
				line-height: 28px;
				height: 28px;
			}
	
	.main-content .el-pagination /deep/ .btn-prev {
				border: none;
				border-radius: 2px;
				padding: 0 5px;
				margin: 0 5px;
				color: inherit;
				background: #f4f4f5;
				display: inline-block;
				vertical-align: top;
				font-size: inherit;
				line-height: 28px;
				min-width: 35px;
				height: 28px;
			}
	
	.main-content .el-pagination /deep/ .btn-next {
				border: none;
				border-radius: 2px;
				padding: 0 5px;
				margin: 0 5px;
				color: inherit;
				background: #f4f4f5;
				display: inline-block;
				vertical-align: top;
				font-size: inherit;
				line-height: 28px;
				min-width: 35px;
				height: 28px;
			}
	
	.main-content .el-pagination /deep/ .btn-prev:disabled {
				border: none;
				cursor: not-allowed;
				border-radius: 2px;
				padding: 0 5px;
				margin: 0 5px;
				color: #aaa;
				background: #f4f4f5;
				display: inline-block;
				vertical-align: top;
				font-size: inherit;
				line-height: 28px;
				height: 28px;
			}
	
	.main-content .el-pagination /deep/ .btn-next:disabled {
				border: none;
				cursor: not-allowed;
				border-radius: 2px;
				padding: 0 5px;
				margin: 0 5px;
				color: #aaa;
				background: #f4f4f5;
				display: inline-block;
				vertical-align: top;
				font-size: inherit;
				line-height: 28px;
				height: 28px;
			}

	.main-content .el-pagination /deep/ .el-pager {
				padding: 0;
				margin: 0;
				display: inline-block;
				vertical-align: top;
				font-size: inherit;
			}

	.main-content .el-pagination /deep/ .el-pager .number {
				cursor: pointer;
				padding: 0 4px;
				margin: 0 5px;
				color: inherit;
				display: inline-block;
				vertical-align: top;
				font-size: inherit;
				line-height: 28px;
				border-radius: 2px;
				background: #f4f4f5;
				text-align: center;
				min-width: 30px;
				height: 28px;
			}
	
	.main-content .el-pagination /deep/ .el-pager .number:hover {
				cursor: pointer;
				padding: 0 4px;
				margin: 0 5px;
				color: #fff;
				display: inline-block;
				vertical-align: top;
				font-size: inherit;
				line-height: 28px;
				border-radius: 2px;
				background: rgba(86,178,198,.8);
				text-align: center;
				min-width: 30px;
				height: 28px;
			}
	
	.main-content .el-pagination /deep/ .el-pager .number.active {
				cursor: default;
				padding: 0 4px;
				margin: 0 5px;
				color: #FFF;
				display: inline-block;
				vertical-align: top;
				font-size: inherit;
				line-height: 28px;
				border-radius: 2px;
				background: rgba(86,178,198,.8);
				text-align: center;
				min-width: 30px;
				height: 28px;
			}
	
	.main-content .el-pagination /deep/ .el-pagination__sizes {
				color: inherit;
				display: inline-block;
				vertical-align: top;
				font-size: inherit;
				line-height: 28px;
				height: 28px;
			}
	
	.main-content .el-pagination /deep/ .el-pagination__sizes .el-input {
				margin: 0 5px;
				color: inherit;
				width: 100px;
				font-size: inherit;
				position: relative;
			}
	
	.main-content .el-pagination /deep/ .el-pagination__sizes .el-input .el-input__inner {
				border: 1px solid #DCDFE6;
				cursor: pointer;
				padding: 0 25px 0 8px;
				color: inherit;
				display: inline-block;
				font-size: inherit;
				line-height: 28px;
				border-radius: 3px;
				outline: 0;
				background: #fff;
				width: 100%;
				text-align: center;
				height: 28px;
			}
	
	.main-content .el-pagination /deep/ .el-pagination__sizes .el-input span.el-input__suffix {
				top: 0;
				position: absolute;
				right: 0;
				height: 100%;
			}
	
	.main-content .el-pagination /deep/ .el-pagination__sizes .el-input .el-input__suffix .el-select__caret {
				cursor: pointer;
				color: #C0C4CC;
				width: 25px;
				font-size: 14px;
				line-height: 28px;
				text-align: center;
			}
	
	.main-content .el-pagination /deep/ .el-pagination__jump {
				margin: 0 0 0 24px;
				color: inherit;
				display: inline-block;
				vertical-align: top;
				font-size: inherit;
				line-height: 28px;
				height: 28px;
			}
	
	.main-content .el-pagination /deep/ .el-pagination__jump .el-input {
				border-radius: 3px;
				padding: 0 2px;
				margin: 0 2px;
				color: inherit;
				display: inline-block;
				width: 50px;
				font-size: inherit;
				line-height: 18px;
				position: relative;
				text-align: center;
				height: 28px;
			}
	
	.main-content .el-pagination /deep/ .el-pagination__jump .el-input .el-input__inner {
				border: 1px solid #DCDFE6;
				cursor: pointer;
				padding: 0 3px;
				color: inherit;
				display: inline-block;
				font-size: inherit;
				line-height: 28px;
				border-radius: 3px;
				outline: 0;
				background: #fff;
				width: 100%;
				text-align: center;
				height: 28px;
			}
	
	// list one
	.one .list1-view {
				border: 0;
				cursor: pointer;
				border-radius: 4px;
				padding: 0 15px;
				margin: 0px 5px 5px 0;
				outline: none;
				clip-path: polygon(0% 0%, 95% 0, 100% 50%, 95% 100%, 0% 100%);
				color: #fff;
				background: rgba(86,178,198,.8);
				width: auto;
				font-size: inherit;
				height: 32px;
			}
	
	.one .list1-view:hover {
				opacity: 0.8;
			}
	
	.one .list1-edit {
				border: 0;
				cursor: pointer;
				border-radius: 4px;
				padding: 0 15px;
				margin: 0px 5px 5px 0;
				outline: none;
				clip-path: polygon(0% 0%, 95% 0, 100% 50%, 95% 100%, 0% 100%);
				color: #fff;
				background: #409eff;
				width: auto;
				font-size: inherit;
				height: 32px;
			}
	
	.one .list1-edit:hover {
				opacity: 0.8;
			}
	
	.one .list1-del {
				border: 0;
				cursor: pointer;
				border-radius: 4px;
				padding: 0 15px;
				margin: 0px 5px 5px 0;
				outline: none;
				clip-path: polygon(0% 0%, 95% 0, 100% 50%, 95% 100%, 0% 100%);
				color: #fff;
				background: rgba(255, 0, 0, 1);
				width: auto;
				font-size: inherit;
				height: 32px;
			}
	
	.one .list1-del:hover {
				opacity: 0.8;
			}
	
	.one .list1-btn8 {
				border: 0;
				cursor: pointer;
				border-radius: 4px;
				padding: 0 24px;
				margin: 0px 5px 5px 0;
				outline: none;
				clip-path: polygon(0% 0%, 95% 0, 100% 50%, 95% 100%, 0% 100%);
				color: #fff;
				background: rgba(255, 128, 0, 1);
				width: auto;
				font-size: inherit;
				height: 32px;
			}
	
	.one .list1-btn8:hover {
				opacity: 0.8;
			}
	
	.main-content .el-table .el-switch {
				display: inline-flex;
				vertical-align: middle;
				line-height: 30px;
				position: relative;
				align-items: center;
				height: 30px;
			}
	.main-content .el-table .el-switch /deep/ .el-switch__label--left {
				cursor: pointer;
				margin: 0 10px 0 0;
				color: #333;
				font-weight: 500;
				display: inline-block;
				vertical-align: middle;
				font-size: 16px;
				transition: .2s;
				height: 30px;
			}
	.main-content .el-table .el-switch /deep/ .el-switch__label--right {
				cursor: pointer;
				margin: 0 0 0 10px;
				color: #333;
				font-weight: 500;
				display: inline-block;
				vertical-align: middle;
				font-size: 16px;
				transition: .2s;
				height: 30px;
			}
	.main-content .el-table .el-switch /deep/ .el-switch__core {
				border: 1px solid rgba(86,178,198,.8);
				cursor: pointer;
				border-radius: 15px;
				margin: 0;
				outline: 0;
				background: rgba(86,178,198,.8);
				display: inline-block;
				width: 50px;
				box-sizing: border-box;
				transition: border-color .3s,background-color .3s;
				height: 24px;
			}
	.main-content .el-table .el-switch /deep/ .el-switch__core::after {
				border-radius: 100%;
				top: 1px;
				left: 1px;
				background: #FFF;
				width: 20px;
				position: absolute;
				transition: all .3s;
				height: 20px;
			}
	.main-content .el-table .el-switch.is-checked /deep/ .el-switch__core::after {
				margin: 0 0 0 -27px;
				left: 100%;
			}
	
	.main-content .el-table .el-rate /deep/ .el-rate__item {
				cursor: pointer;
				display: inline-block;
				vertical-align: middle;
				font-size: 0;
				position: relative;
			}
	.main-content .el-table .el-rate /deep/ .el-rate__item .el-rate__icon {
				margin: 0 3px;
				color: #666;
				display: inline-block;
				font-size: 18px;
				position: relative;
				transition: .3s;
			}
</style>
