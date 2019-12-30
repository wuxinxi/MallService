# -*- coding: UTF-8 -*-
"""
@author: TangRen
@time: 2019/12/28 16:35
@file: responseSchedule.py
@desc: 相应调度

"""
from shopping.response import HttpCode


def check(params):
    if params is None or not params.strip():
        return {'code': HttpCode.HTTP_INVALID_PARAMS, 'message': '参数缺省!'}
        pass
