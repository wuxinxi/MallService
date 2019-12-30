# -*- coding: UTF-8 -*-
'''
@author: TangRen
@time: 2019/12/30
@file: card_goods_serializes.py
@desc: 购物车

'''

from shopping.models import CardGoods
from rest_framework import serializers


class CardGoodsSerializers(serializers.ModelSerializer):
    class Meta:
        model = CardGoods
        exclude = ('id', 'userTable')

