#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：backend
@File    ：online_version.py
@Author  ：吕星澎
@Date    ：2022/12/3 20:48
"""
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from dvadmin.project.models import OnlineCurrentTime
from dvadmin.utils.json_response import SuccessResponse, DetailResponse
from dvadmin.utils.serializers import CustomModelSerializer
from dvadmin.utils.viewset import CustomModelViewSet


class DemandSerializer(CustomModelSerializer):
    """
    上线版本序列化器
    """

    class Meta:
        model = OnlineCurrentTime
        fields = "__all__"
        read_only_fields = ['id']


class DemandCreateUpdateSerializer(CustomModelSerializer):
    """
    创建/更新时的列化器
    """
    print("上线版本创建/更新时序列化器")

    class Meta:
        model = OnlineCurrentTime
        fields = '__all__'


class DemandViewSet(CustomModelViewSet):
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = OnlineCurrentTime.objects.all()  # 指明该视图集在查询数据时使用的查询集
    serializer_class = DemandSerializer  # 指明该视图在记性序列化或者反序列化时使用的序列化器
