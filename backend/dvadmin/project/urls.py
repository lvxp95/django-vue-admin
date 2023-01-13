#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：backend 
@File    ：urls.py
@Author  ：吕星澎
@Date    ：2022/12/3 21:45 
'''
from rest_framework.routers import SimpleRouter

from dvadmin.project.views.online_version import OnlineVersionViewSet

router = SimpleRouter()
router.register(r'online_version', OnlineVersionViewSet)

urlpatterns = [
]
urlpatterns += router.urls
