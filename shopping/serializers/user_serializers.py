# -*- coding: UTF-8 -*-
"""
@author: TangRen
@time: 2019/12/28 17:31
@file: user_serializers.py
@desc: 用户

"""
from shopping.models import UserTable
from rest_framework import serializers


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserTable
        # 排除id以及密码
        exclude = ('id', 'user_pwd',)


class SaveUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserTable
        fields = '__all__'
