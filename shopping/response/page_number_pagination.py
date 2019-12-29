# -*- coding: UTF-8 -*-
"""
@author: TangRen
@time: 2019-07-15
@file: page_number_pagination.py
@desc: 页码分页，并自定义返回信息
需要在setting。py 进行设置
"""
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict


class StandardResultsSetPagination(PageNumberPagination):
    # 默认每页显示的数据条数
    page_size = 1

    # 获取URL参数设置的每页数据条数
    page_size_query_param = 'page_size'

    # 获取URL参数中传入的页数
    page_query_param = 'page'

    # 最大支持的每页显示条数
    max_page_size = 10

    # 最后一页显示字符串
    last_page_strings = ('the end',)

    # 无效页面
    invalid_page_message = '请求页不存在'

    def get_paginated_response(self, data):
        code = 200
        message = 'success'
        if not data:
            code = 404
            message = 'data not found'
        print(code)
        return Response(OrderedDict([
            ('code', code),
            ('message', message),
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('data', data),
        ]))
