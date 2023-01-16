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
      <div class="box-content">
        <transition name="box-content-left">
          <div class="box-content-left" />
        </transition>
        <div class="box-content-right">
          <div>
            <transition name="table">
              <table class="table">
                <thead>
                <tr>
                  <th :key="index" v-for="(item, index) of systems">{{ item }}</th>
                </tr>
                </thead>
                <tr :key="index" v-for="(item, index) of dataList">
                  <td>{{ titleList[index] }}</td>
                  <td>{{ item[0] }}</td>
                  <td>{{ item[1] }}</td>
                  <td>{{ item[2] }}</td>
                  <td>{{ item[3] }}</td>
                  <td>{{ item[4] }}</td>
                </tr>
                <!--              </transition-group>-->
              </table>
            </transition>
          </div>
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
      systems: [],
      dataList: [],
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
    query () {
      if (this.year_month === '' || this.year_month === null || this.version_number === '') {
        Message({
          message: '年月与批次号不能为空',
          type: 'error',
          duration: 5 * 1000
        })
      } else {
        return api.searchByOnlineVersion({ yearMonth: this.year_month, versionNumber: this.version_number }).then((res) => {
          const lineRace1 = echarts.init(document.querySelector('.box-content-left'))
          this.data = res.data.data
          const dataList = new Array(15)
          for (let i = 0; i < dataList.length; ++i) {
            dataList[i] = []
          }
          this.systems = ['状态']
          this.data.forEach((val) => {
            this.systems.push(val.system)
            dataList[0].push(val.count)
            dataList[1].push(val.undeveloped)
            dataList[2].push(val.unpublished)
            dataList[3].push(val.not_configured)
            dataList[4].push(val.demand_not_confirmed)
            dataList[5].push(val.block)
            dataList[6].push(val.joint_commissioning)
            dataList[7].push(val.not_tested)
            dataList[8].push(val.under_test)
            dataList[9].push(val.test_pass)
            dataList[10].push(val.test_fail)
            dataList[11].push(val.fixed)
            dataList[12].push(val.unable_to_test)
            dataList[13].push(val.not_online_temporarily)
            dataList[14].push(val.already_online)
          })
          this.dataList = dataList
          const titleList = ['总数', '未开发完成', '未发布', '未配置', '需求未确认', '阻塞', '联调中', '未测试', '测试中', '通过', '未通过',
            '已修复', '通过（无法测试）', '暂不上线', '已经上线']
          this.titleList = titleList
          const series = []
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
          lineRace1.setOption({
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
              data: this.systems
            },
            series: series
          })
        })
      }
    }
  }
}
</script>

<style lang="less" scoped>
@itemBg: #FFFFFF;
@itemBorder: #B1B0B0FF;
.box {
  margin-top: 20px;
  display: flex;
  flex-flow: column;
  overflow: hidden;
  &-content {
    width: 100%;
    height: 45%;
    margin-top: 20px;
    display: flex;
    flex-flow: row;
    &-left {
      height: 400px;
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

  }

}
.table {
  width: 100%;
  font-size: 16px;
  background: @itemBg;
  color: #5f6166;
  border: 0 solid @itemBorder;
  border-top: none;
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
      border: 1px solid @itemBorder;
    }
    td {
      padding: 5px 10px;
      width: 100px;
      white-space: nowrap;
      text-align: center;
      border: 1px solid @itemBorder;
    }
  }
  &-tbody {
    &-enter-active {
      animation: flipInY 0.5s;
    }
  }
}
</style>
