#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：backend
@File    ：online_version.py
@Author  ：吕星澎
@Date    ：2022/12/3 20:48
"""
import os
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from application import settings
from dvadmin.project.models import OnlineVersionStatistics
from dvadmin.utils.json_response import SuccessResponse
from dvadmin.utils.serializers import CustomModelSerializer
from dvadmin.utils.viewset import CustomModelViewSet
import openpyxl

svn_settings = settings.SVN_SETTINGS
svn_dir_name = settings.SVN_DIR_NAME


class OnlineVersionSerializer(CustomModelSerializer):
    """
    上线版本序列化器
    """

    class Meta:
        model = OnlineVersionStatistics
        fields = "__all__"
        # fields = ["online_version"]


# class CrudDemoModelCreateUpdateSerializer(CustomModelSerializer):
#     """
#     创建/更新时的列化器
#     """
#     print("上线版本创建/更新时序列化器")
#
#     class Meta:
#         model = OnlineVersion
#         fields = '__all__'


def checkout():
    cmd = 'svn export %(url)s %(dist)s --username %(user)s --password %(pwd)s' % svn_settings
    print("execute %s" % cmd)
    return os.system(cmd)


class OnlineVersionViewSet(CustomModelViewSet):
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """

    # os.chdir(svn_settings['svn'])
    # checkout()
    queryset = OnlineVersionStatistics.objects.filter(online_version='2021-10-26')  # 指明该视图集在查询数据时使用的查询集
    serializer_class = OnlineVersionSerializer  # 指明该视图在记性序列化或者反序列化时使用的序列化器
    filter_fields = ['online_version']
    search_fields = ['equest_number']

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
        year = request.data['yearMonth'].split('-')[0]
        month = request.data['yearMonth'].split('-')[1]
        version_number = request.data['versionNumber']
        setting = {'year': year, 'month': month, 'version_number': version_number}
        url = '%(year)s年辽宁移动系统升级_%(month)月_01/%(year)s年辽宁移动系统升级_%(month)s_%(version_number)s.xlsx' % setting
        setting = svn_settings.copy()
        setting['url'] += url
        print(svn_settings['url'])
        print(setting['url'])
        setting['dist'] = os.getcwd() + '\static\svn_file'
        os.system('svn export %(url)s %(dist)s --username %(user)s --password %(pwd)s' % setting)


        data = {}
        return SuccessResponse(data=data)

    @action(methods=["GET"], detail=False, permission_classes=[])
    def count_by_online_version(self, request):
        value = "count_by_online_version"
