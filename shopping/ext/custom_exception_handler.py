# -*- coding: UTF-8 -*-
'''
@author: TangRen
@time: 2019/12/31
@file: custom_exception_handler.py
@desc: 自定义异常

'''
from rest_framework.views import exception_handler

from rest_framework.response import Response


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        response.data.clear()
        response.data['code'] = response.status_code

        # message = response.data["detail"] if 'detail' in response.data else None

        if response.status_code == 404:
            response.data['message'] = '接口走丢了!'

        if response.status_code == 400:
            response.data['message'] = '请求无效!'

        elif response.status_code == 401:
            response.data['message'] = "授权失败!"

        elif response.status_code >= 500:
            response.data['message'] = "攻城狮努力恢复中!"

        elif response.status_code == 403:
            response.data['message'] = "认证失败"

        elif response.status_code == 405:
            response.data['message'] = '请求方法错误'
        else:
            response.data['message'] = str(exc)
        return response
    # else:
    #     response = Response({'code': -1, 'message': str(exc)})
    # return response
