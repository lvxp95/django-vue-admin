#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：backend
@File    ：online_version.py
@Author  ：吕星澎
@Date    ：2022/12/3 20:48
"""
import os
from application import settings
import xlrd
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from dvadmin.utils.json_response import SuccessResponse, DetailResponse
from dvadmin.utils.viewset import CustomModelViewSet

svn_settings = settings.SVN_SETTINGS
svn_dir_name = settings.SVN_DIR_NAME


def get_statistics_data(online_data, online_version_dct, development, test_result):
    online_version_dct['count'] += 1
    if online_data[test_result] == '未开发完毕':
        online_version_dct['undeveloped'] += 1
    elif online_data[development] == '未发布' and online_data[test_result] == '未测试':
        online_version_dct['unpublished'] += 1
    elif online_data[test_result] in ["产品未配置", "开通未配置", "计费未配置", "其他未配置"]:
        online_version_dct['not_configured'] += 1
    elif online_data[test_result] == '需求未确认':
        online_version_dct['demand_not_confirmed'] += 1
    elif online_data[test_result] == '阻塞':
        online_version_dct['block'] += 1
    elif online_data[test_result] == '联调中':
        online_version_dct['joint_commissioning'] += 1
    elif online_data[development] in ["已发布", "无需发布"] and online_data[test_result] == '未测试':
        online_version_dct['not_tested'] += 1
    elif online_data[development] in ["已发布", "无需发布"] and online_data[test_result] == '测试中':
        online_version_dct['under_test'] += 1
    elif online_data[test_result] == '通过':
        online_version_dct['test_pass'] += 1
    elif online_data[test_result] == '不通过':
        online_version_dct['test_fail'] += 1
    elif online_data[development] == "已发布" and online_data[test_result] in ["已修复待发布", "已修复待验证"]:
        online_version_dct['fixed'] += 1
    elif online_data[test_result] == '通过（无法测试）':
        online_version_dct['unable_to_test'] += 1
    elif online_data[test_result] == '暂不上线':
        online_version_dct['not_online_temporarily'] += 1
    elif online_data[test_result] == '已经上线':
        online_version_dct['already_online'] += 1
    return online_version_dct


def get_employee_info_data(file_path, version_number):
    dev_environment_162 = 'ost_development'
    test_environment_162 = 'ost_test_result'
    dev_environment_143 = 'oft_development'
    test_environment_143 = 'oft_test_result'
    employee_data = []
    t_online_statistics_162 = []
    t_online_statistics_143 = []
    systems = []
    work_book = xlrd.open_workbook(file_path)
    sheet = work_book.sheet_by_name('上线清单')
    for i in range(1, sheet.nrows):
        t_dct = {
            'equest_number': sheet.cell(i, 1).value,
            'demand_number': sheet.cell(i, 2).value,
            'systems': sheet.cell(i, 3).value,
            'requirements': sheet.cell(i, 4).value,
            'demand_type': sheet.cell(i, 5).value,
            'demand_source': sheet.cell(i, 6).value,
            'bureau_manager': sheet.cell(i, 7).value,
            'demand_complexity': sheet.cell(i, 8).value,
            'demand_manager': sheet.cell(i, 9).value,
            'development_manager': sheet.cell(i, 14).value,
            'development_group_leader': sheet.cell(i, 15).value,
            'tester': sheet.cell(i, 16).value,
            'ost_development': sheet.cell(i, 20).value,
            'ost_test_result': sheet.cell(i, 21).value,
            'oft_development': sheet.cell(i, 22).value,
            'oft_test_result': sheet.cell(i, 23).value,
            'notes': sheet.cell(i, 8).value,
            'version_number': version_number,
        }
        if t_dct['systems'] not in systems:
            systems.append(t_dct['systems'])
            online_version_dct_162 = {'system': t_dct['systems'], 'count': 0, 'undeveloped': 0, 'unpublished': 0,
                                      'not_configured': 0, 'demand_not_confirmed': 0, 'block': 0,
                                      'joint_commissioning': 0,
                                      'not_tested': 0, 'under_test': 0, 'test_pass': 0, 'test_fail': 0, 'fixed': 0,
                                      'unable_to_test': 0, 'not_online_temporarily': 0, 'already_online': 0}
            online_version_dct_143 = online_version_dct_162.copy()
            t_online_statistics_162.append(online_version_dct_162)
            t_online_statistics_143.append(online_version_dct_143)
        else:
            online_version_dct_162 = [online_version_dct for online_version_dct in t_online_statistics_162
                                      if online_version_dct['system'] == t_dct['systems']][0]
            online_version_dct_143 = [online_version_dct for online_version_dct in t_online_statistics_143
                                      if online_version_dct['system'] == t_dct['systems']][0]

        dct = get_statistics_data(t_dct, online_version_dct_162, dev_environment_162, test_environment_162)
        index = [index for index, dct in enumerate(t_online_statistics_162) if dct['system'] == t_dct['systems']][0]
        t_online_statistics_162[index] = dct
        dct = get_statistics_data(t_dct, online_version_dct_143, dev_environment_143, test_environment_143)
        index = [index for index, dct in enumerate(t_online_statistics_143) if dct['system'] == t_dct['systems']][0]
        t_online_statistics_143[index] = dct
        employee_data.append(t_dct)

    return employee_data, t_online_statistics_162, t_online_statistics_143


class OnlineViewSet(CustomModelViewSet):
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    @action(methods=["POST"], detail=False, permission_classes=[IsAuthenticated])
    def select_version_number(self, request):
        locale_path = os.getcwd() + '\static\svn_file_info.txt'
        year = request.data['yearMonth'].split('-')[0]
        month = request.data['yearMonth'].split('-')[1]
        svn_dir = svn_dir_name % (year, month)
        svn_address = 'http://10.65.7.148/svn/LNcrm/ln-doc/辽宁移动系统升级/%s' % svn_dir
        os.system('svn list %s >> %s' % (svn_address, locale_path))
        file_name_ls = [line.strip() for line in open('static/svn_file_info.txt', encoding='gbk')]  # 获取目录下的所有文件名
        data = [file_name for file_name in file_name_ls if file_name.find('年辽宁移动系统升级') != -1]  # 获取符合要求的名称列表
        version_num_ls = [file_name.split('_')[-1].split('.')[0] for file_name in data]  # 获取批次号
        os.remove(locale_path)
        return SuccessResponse(data=version_num_ls)

    @action(methods=["POST"], detail=False, permission_classes=[IsAuthenticated])
    def search_by_online_version(self, request):
        # 设置svn语句
        year = request.data['yearMonth'].split('-')[0]
        month = request.data['yearMonth'].split('-')[1]
        version_number = request.data['versionNumber']
        online_version = request.data['yearMonth'] + '-' + version_number
        setting = {'year': year, 'month': month, 'version_number': str(version_number)}
        file_path = '%(year)s年辽宁移动系统升级_%(month)s月_01/' % setting
        file_name = '%(year)s年辽宁移动系统升级_%(month)s_%(version_number)s.xlsx' % setting
        url = file_path + file_name
        setting = svn_settings.copy()
        setting['url'] += url
        setting['dist'] = os.getcwd() + '\static\svn_file'

        # 从svn检查文件
        cmd = 'svn export \"%(url)s\" %(dist)s --username %(user)s --password %(pwd)s' % setting
        os.system(cmd)

        # 获取上线清单内容和统计数据
        data, t_online_statistics_162, t_online_statistics_143 = get_employee_info_data(setting['dist'] + '\\' +
                                                                                        file_name, online_version)
        # self.get_queryset().filter(version_number=online_version).delete()
        # serializer_class = self.get_serializer_class()
        # serializer = serializer_class(data=data, many=True)
        # try:
        #     serializer.is_valid(raise_exception=True)
        # except Exception as e:
        #     print(e)
        #     os.remove(setting['dist'] + '\\' + file_name)
        #     return DetailResponse(data={'162': [], '143': []}, msg="数据校验失败： "+e)
        # serializer.save()
        os.remove(setting['dist'] + '\\' + file_name)
        return SuccessResponse(data={'162': t_online_statistics_162, '143': t_online_statistics_143}, msg="获取成功")
