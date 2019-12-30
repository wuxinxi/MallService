# -*- coding: UTF-8 -*-
'''
@author: TangRen
@time: 2019/12/30
@file: card_goods_serializes.py
@desc: 购物车

'''

from shopping.models import GoodsInfo, GoodsBanner
from rest_framework import serializers


class GoodsBannerSerializers(serializers.ModelSerializer):
    class Meta:
        model = GoodsBanner
        fields = ('url',)


class GoodsInfoSerializes(serializers.ModelSerializer):
    banner = GoodsBannerSerializers(many=True)
    class Meta:
        model = GoodsInfo
        exclude = ('id',)
