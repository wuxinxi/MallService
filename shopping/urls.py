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
    path('userCenter/reset', sp.Reset.as_view()),
    path('userCenter/getVerifyCode', sp.PhoneVerify.as_view()),
    path('userCenter/getMessage', sp.MessageInfo.as_view()),
    path('userCenter/getCardGoods', sp.CardGood.as_view()),
    path('userCenter/cardGoodsManage', sp.CardGoodsManager.as_view()),
    path('common/getCategoryList', sp.CategoryList.as_view()),
    path('common/getGoodsInfoList', sp.GoodInfoList.as_view()),
    path('userCenter/getShipAddress', sp.ShipAddressList.as_view()),
    path('userCenter/shipAddressManage', sp.ShipAddressManage.as_view()),
]
