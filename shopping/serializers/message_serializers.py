# -*- coding: UTF-8 -*-
'''
@author: TangRen
@time: 2019/12/30
@file: message_serializers.py
@desc: 消息序列号

'''
from shopping.models import MessageInfo
from rest_framework import serializers


class MessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = MessageInfo
        exclude = ('id', 'userTable')
