#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：backend
@File    ：urls.py
@Author  ：吕星澎
@Date    ：2022/12/3 21:45
"""
from django.urls import path
from rest_framework.routers import SimpleRouter
from dvadmin.project.views.online_version import OnlineViewSet
from dvadmin.project.views.demand import DemandViewSet

router = SimpleRouter()
router.register(r'demand', DemandViewSet)

urlpatterns = [
    path('online/search_by_online_version/', OnlineViewSet.as_view({'post': 'search_by_online_version'})),
    path('online/select_version_number/', OnlineViewSet.as_view({'post': 'select_version_number'})),
]
urlpatterns += router.urls
