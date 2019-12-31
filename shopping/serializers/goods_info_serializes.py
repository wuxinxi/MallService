# -*- coding: UTF-8 -*-
'''
@author: TangRen
@time: 2019/12/30
@file: card_goods_serializes.py
@desc: 商品信息

'''

from shopping.models import GoodsInfo, GoodsBanner, GoodsSku
from rest_framework import serializers


class GoodsBannerSerializers(serializers.ModelSerializer):
    """
    商品轮播图
    """

    class Meta:
        model = GoodsBanner
        fields = ('url',)


class GoodsSkuSerializers(serializers.ModelSerializer):
    """
    商品属性
    """

    class Meta:
        model = GoodsSku
        fields = ('goods_sku_title', 'goods_sku_content',)


class GoodsInfoSerializes(serializers.ModelSerializer):
    banner = GoodsBannerSerializers(many=True)
    sku = GoodsSkuSerializers(many=True)

    class Meta:
        model = GoodsInfo
        exclude = ('id',)
