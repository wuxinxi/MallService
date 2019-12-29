# -*- coding: UTF-8 -*-
"""
@author: TangRen
@time: 2019/12/28 15:24
@file: urls.py
@desc: 路由

"""
from django.urls import path
import shopping.views as  sp

urlpatterns = [
    path('userCenter/register', sp.Register.as_view()),
    path('userCenter/login', sp.Login.as_view()),
    path('userCenter/getVerifyCode', sp.PhoneVerify.as_view())
]
