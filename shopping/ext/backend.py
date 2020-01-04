# -*- coding: UTF-8 -*-
'''
@author: TangRen
@time: 2020/1/4
@file: backend.py
@desc: 自定义modelBackend

'''
from django.contrib.auth.backends import ModelBackend
from shopping.models import UserTable
from django.db.models import Q


class ShoppingBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 用户名或者手机号均可登录
            user = UserTable.objects.get(Q(Q(user_name=username) | Q(user_mobile=username)) & Q(user_pwd=password))
            return user
        except:
            return None
