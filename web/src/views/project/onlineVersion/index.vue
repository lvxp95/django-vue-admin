<template>
  <d2-container>
    <div class="box">
      <div class="box-header">
        <span class="demonstration">上线版本（年月）</span>
        <el-date-picker
          v-model="year_month"
          type="month"
          placeholder="选择年月"
          value-format="yyyy-MM"
          @change = "dateOfSelection"
        />
        <el-select v-model="version_number" class="m-2" placeholder="批次号" clearable size="large" style="margin-left: 20px">
          <el-option
            v-for="item in version_num_ls"
            :key="item"
            :value="item"
          />
        </el-select>
        <el-button type="primary" @click="query" style="margin-left: 20px">查询</el-button>
      </div>
      <div class="box-content1">
        <transition name="box-content1-left">
          <div class="box-content1-left" />
        </transition>
        <div class="box-content1-right">
          <transition name="table">
            <table class="table">
              <thead>
              <tr>
                <th v-if="dataList162.length !== 0">状态</th>
                <th :key="index" v-for="(item, index) of systems162">{{ item }}</th>
              </tr>
              </thead>
              <tr :key="index" v-for="(item, index) of dataList162">
                <td>{{ titleList[index] }}</td>
                <td :key="index" v-for="index of systems162.length">{{ item[index-1] }}</td>
              </tr>
            </table>
          </transition>
        </div>
      </div>
      <div class="box-content2">
        <transition name="box-content2-left">
          <div class="box-content2-left" />
        </transition>
        <div class="box-content2-right">
          <transition name="table">
            <table class="table">
              <thead>
              <tr>
                <th v-if="dataList143.length !== 0">状态</th>
                <th :key="index" v-for="(item, index) of systems143">{{ item }}</th>
              </tr>
              </thead>
              <tr :key="index" v-for="(item, index) of dataList143">
                <td>{{ titleList[index] }}</td>
                <td :key="index" v-for="index of systems162.length">{{ item[index-1] }}</td>
              </tr>
            </table>
          </transition>
        </div>
      </div>
    </div>
  </d2-container>
</template>

<script>
import * as api from './api'
import * as echarts from 'echarts'
import { ref } from 'vue'
import { Message } from 'element-ui'

export default {
  name: 'online_version',
  mounted () {
  },
  data () {
    return {
      systems162: [],
      systems143: [],
      dataList162: [],
      dataList143: [],
      titleList: [],
      year_month: ref(''),
      version_num_ls: [],
      version_number: ref('')
    }
  },
  methods: {
    dateOfSelection (val) {
      this.version_num_ls = []
      if (val != null) {
        return api.selectVersionNumber(val).then(res => {
          const { data } = res.data
          this.version_num_ls = data
        })
      }
    },
    generateData (data, titleList, lineRace) {
      const dataList = new Array(15)
      const systems = []
      const series = []
      for (let i = 0; i < dataList.length; ++i) {
        dataList[i] = []
      }
      // 生成按系统分组的统计数据列表
      data.forEach((val) => {
        systems.push(val.system)
        for (let i = 1; i < dataList.length; i++) {
          dataList[i].push(val[Object.keys(val)[i + 1]])
        }
      })
      for (let i = 1; i < dataList.length; ++i) {
        series.push({
          name: titleList[i],
          type: 'bar',
          stack: 'total',
          label: {
            show: true
          },
          emphasis: {
            focus: 'series'
          },
          data: dataList[i]
        })
      }
      lineRace.setOption({
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            // Use axis to trigger tooltip
            type: 'shadow' // 'shadow' as default; can also be 'line' or 'shadow'
          }
        },
        legend: {},
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: {
          type: 'value'
        },
        yAxis: {
          type: 'category',
          data: systems
        },
        series: series
      })
      return { dataList: dataList, systems: systems }
    },
    query () {
      if (this.year_month === '' || this.year_month === null || this.version_number === '') {
        Message({
          message: '年月与批次号不能为空',
          type: 'error',
          duration: 5 * 1000
        })
      } else {
        return api.searchByOnlineVersion({ yearMonth: this.year_month, versionNumber: this.version_number }).then((res) => {
          this.data162 = res.data.data['162']
          this.data143 = res.data.data['143']
          this.titleList = ['总数', '未开发完成', '未发布', '未配置', '需求未确认', '阻塞', '联调中', '未测试', '测试中', '通过', '未通过',
            '已修复', '通过（无法测试）', '暂不上线', '已经上线']
          let value = {}
          value = this.generateData(this.data162, this.titleList, echarts.init(document.querySelector('.box-content1-left')))
          this.dataList162 = value.dataList
          this.systems162 = value.systems
          value = this.generateData(this.data143, this.titleList, echarts.init(document.querySelector('.box-content2-left')))
          this.dataList143 = value.dataList
          this.systems143 = value.systems
        })
      }
    }
  }
}
</script>

<style lang="less" scoped>
@itemBg: #FFFFFF;
@itemBorder: #0bb0ee;
.box {
  margin-top: 20px;
  display: flex;
  flex-flow: column;
  overflow: hidden;
  &-content1 {
    width: 100%;
    height: 55vh;
    margin-top: 20px;
    margin-bottom: 20px;
    display: flex;
    flex-flow: row;
    &-left {
      width: 60%;
      color: white;
      display: flex;
      flex-flow: column;
      &-enter-active {
        animation: fadeIn 0.25s;
      }
      &-leave-active {
        animation: fadeOut 0.25s;
      }
    }
    &-right {
      height: auto;
    }

  }
  &-content2 {
    width: 100%;
    height: 55vh;
    margin-top: 20px;
    display: flex;
    flex-flow: row;
    &-left {
      width: 60%;
      color: white;
      display: flex;
      flex-flow: column;
      &-enter-active {
        animation: fadeIn 0.25s;
      }
      &-leave-active {
        animation: fadeOut 0.25s;
      }
    }
    &-right {
      height: auto;
      width: auto;
    }

  }

}
.table {
  background: @itemBg;
  color: #5f6166;
  //border-bottom: 0 solid @itemBorder;
  //border-top: none;
  border-spacing: 0;
  &-enter-active {
    animation: fadeIn 0.25s;
  }
  &-leave-active {
    animation: fadeOut 0.25s;
  }
  tr {
    th {
      padding: 5px;
      white-space: nowrap;
      border-bottom: 3px solid @itemBorder;
    }
    td {
      padding: 5px 10px;
      white-space: nowrap;
      text-align: center;
      border-bottom: 1px solid ;
    }
  }
  &-tbody {
    &-enter-active {
      animation: flipInY 0.5s;
    }
  }
}
</style>
