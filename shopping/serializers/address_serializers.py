# -*- coding: UTF-8 -*-
'''
@author: TangRen
@time: 2019/12/31
@file: address_serializers.py
@desc: 

'''
from shopping.models import ShipAddress
from rest_framework import serializers


class ShipAddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShipAddress
        exclude = ('userTable',)
