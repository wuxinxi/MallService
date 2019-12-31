# -*- coding: UTF-8 -*-
'''
@author: TangRen
@time: 2019/12/31
@file: custom_exception_handler.py
@desc: 自定义异常

'''
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        response.data.clear()
        response.data['code'] = response.status_code
        response.data['data'] = []

        if response.status_code == 404:
            try:
                response.data['message'] = response.data.pop('detail')
                response.data['message'] = 'Not found'
            except:
                response.data['message'] = 'Not found'
        if response.status_code == 400:
            response.data['message'] = 'Input error'

        elif response.status_code == 401:
            response.data['message'] = "Auth failed"

        elif response.status_code >= 500:
            response.data['message'] = "Internal service errors"

        elif response.status_code == 403:
            response.data['message'] = "Access denied"

        elif response.status_code == 405:
            response.data['message'] = 'Request method error'
        else:
            response.data['message'] = 'Unknown error'
        return response
