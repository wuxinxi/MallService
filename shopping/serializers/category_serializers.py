# -*- coding: UTF-8 -*-
'''
@author: TangRen
@time: 2019/12/30
@file: category_serializers.py
@desc: 商品分类

'''

from shopping.models import Category
from rest_framework import serializers


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields='__all__'
