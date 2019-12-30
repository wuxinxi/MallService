from django.db.models import Q
from django.shortcuts import render

from rest_framework.decorators import api_view

from rest_framework.views import APIView
from rest_framework.response import Response

from shopping.response import HttpCode
from shopping.serializers.user_serializers import UserSerializers, SaveUserSerializers
from shopping.serializers.message_serializers import MessageSerializers
from shopping.serializers.card_goods_serializes import CardGoodsSerializers
from shopping.serializers.category_serializers import CategorySerializers
from shopping.serializers.goods_info_serializes import GoodsInfoSerializes
from shopping.models import UserTable, MessageInfo, CardGoods, Category, GoodsInfo
import random, string, time
import traceback


# Create your views here.

class Register(APIView):
    """
    注册
    """

    def post(self, request, format=None):
        params = request.data
        user_name = params.get('user_name')
        user_pwd = params.get('user_pwd')
        user_mobile = params.get('user_mobile')

        if user_name is None or user_pwd is None or user_mobile is None:
            return Response({'code': HttpCode.HTTP_INVALID_PARAMS, 'message': '参数缺省!'})
        else:
            user = SaveUserSerializers(data=params)
            if user.is_valid():
                # 使用Q对象可进行&、|操作
                # 如果用户名或者手机号已被注册
                res = UserTable.objects.filter(Q(user_name=user_name) | Q(user_mobile=user_mobile))
                if res.count() != 0:
                    return Response({'code': HttpCode.HTTP_PUSH_ERROR, 'message': '此手机号或者用户名已被注册!'})
                else:
                    res = user.save()
                    return Response({'code': HttpCode.HTTP_SUCCESS, 'message': '注册成功!',
                                     'data': UserSerializers(res, many=False, ).data})
            else:
                return Response({'code': HttpCode.HTTP_INVALID_PARAMS, 'message': '参数无效!'})


class PhoneVerify(APIView):
    """
    模拟手机验证码
    """

    def post(self, request):
        params = request.data
        user_mobile = params.get('user_mobile')
        if user_mobile is None or not user_mobile.strip():
            return Response({'code': HttpCode.HTTP_INVALID_PARAMS, 'message': '参数缺省!'})
        else:
            nums = string.digits
            verify_code = random.choices(nums, k=6)
            return Response(
                {'code': HttpCode.HTTP_SUCCESS, 'message': '验证码已发送,请注意查收!' + user_mobile,
                 'data': "".join(verify_code)}
            )


class Login(APIView):
    """
    登陆
    """

    def post(self, request, format=None):
        params = request.data
        user_name = params.get('user_name')
        user_pwd = params.get('user_pwd')
        if user_name is None or user_pwd is None:
            return Response({'code': HttpCode.HTTP_INVALID_PARAMS, 'message': '参数缺省!'})
        else:
            user = UserTable.objects.filter(user_name=user_name, user_pwd=user_pwd)
            if user.count() != 0:
                return Response(
                    {'code': HttpCode.HTTP_SUCCESS, 'message': '登录成功',
                     'data': UserSerializers(user.first(), many=False, ).data})
            else:
                return Response({'code': HttpCode.HTTP_DATA_NULL, 'message': '用户不存在!'})


class MessageInfo(APIView):
    """
    消息接口
    """

    def get(self, request):
        params = request.data
        user_mobile = params.get('user_mobile')
        if user_mobile is None or not user_mobile.strip():
            return Response({'code': HttpCode.HTTP_INVALID_PARAMS, 'message': '参数缺省!'})
        try:
            user = UserTable.objects.get(user_mobile=user_mobile)
            messageList = user.messageinfo_set.all()
            if messageList.count() == 0:
                return Response({'code': HttpCode.HTTP_DATA_NULL, 'message': '暂时没有任何消息!'})
            else:
                return Response(
                    {'code': HttpCode.HTTP_SUCCESS, 'message': '成功',
                     'data': MessageSerializers(messageList, many=True).data})
        except:
            return Response({'code': HttpCode.HTTP_INVALID_PARAMS, 'message': '账号不存在!'})


class CardGood(APIView):
    """
    购物车接口
    """

    def get(self, request):
        params = request.data
        user_mobile = params.get('user_mobile')
        if user_mobile is None or not user_mobile.strip():
            return Response({'code': HttpCode.HTTP_INVALID_PARAMS, 'message': '参数缺省!'})
        try:
            user = UserTable.objects.get(user_mobile=user_mobile)
            goodsList = user.cardgoods_set.all()
            if goodsList.count() == 0:
                return Response({'code': HttpCode.HTTP_DATA_NULL, 'message': '还未添加任何商品到购物车!'})
            else:
                return Response(
                    {'code': HttpCode.HTTP_SUCCESS, 'message': '成功',
                     'data': CardGoodsSerializers(goodsList, many=True).data})
        except:
            return Response({'code': HttpCode.HTTP_INVALID_PARAMS, 'message': '账号不存在!'})


class AddCardGoods(APIView):
    """
    加入购物车
    """

    def post(self, request):
        params = request.data
        user_mobile = params.get('user_mobile')
        if user_mobile is None or not user_mobile.strip():
            return Response({'code': HttpCode.HTTP_INVALID_PARAMS, 'message': '参数缺省!'})
        res = UserTable.objects.filter(user_mobile=user_mobile)
        if res.count() == 0:
            return Response({'code': HttpCode.HTTP_INVALID_PARAMS, 'message': '账号不存在!'})
        try:
            goods_id = params.get('goods_id')
            goods_desc = params.get('goods_desc')
            goods_icon = params.get('goods_icon')
            goods_price = params.get('goods_price')
            goods_count = params.get('goods_count')
            goods_sku = params.get('goods_sku')

            cardGoods = CardGoods(goods_id=goods_id, goods_desc=goods_desc, goods_icon=goods_icon,
                                  goods_price=goods_price, goods_count=goods_count, goods_sku=goods_sku)
            user = res.first()
            cardGoods.userTable = user
            dbCardGoods = CardGoods.objects.filter(goods_id=goods_id).first()
            message = '保存成功'
            if dbCardGoods is None:
                '新增'
                cardGoods.save()
            else:
                '修改'
                message = '修改成功'
                cardGoods.id = dbCardGoods.id
                cardGoods.save(force_update=True)
            return Response(
                {'code': HttpCode.HTTP_SUCCESS, 'message': message,
                 'data': CardGoodsSerializers(cardGoods).data})
        except Exception as e:
            return Response({'code': HttpCode.HTTP_EX, 'message': ('%s') % e.args})


class CategoryList(APIView):
    """
    分类列表
    """

    def get(self, request):
        categoryList = Category.objects.all()
        if categoryList.count() == 0:
            return Response({'code': HttpCode.HTTP_DATA_NULL, 'message': '还未添加任何商品分类!'})
        else:
            return Response(
                {'code': HttpCode.HTTP_SUCCESS, 'message': "成功",
                 'data': CategorySerializers(categoryList, many=True).data})


class GoodInfoList(APIView):
    """
    商品列表
    """

    def get(self, request):
        params = request.data
        categoryId = params.get('id')
        if categoryId is None or not categoryId.strip():
            return Response({'code': HttpCode.HTTP_INVALID_PARAMS, 'message': '参数缺省!'})
        categoryList = Category.objects.filter(id=categoryId)
        if categoryList.count() == 0:
            return Response({'code': HttpCode.HTTP_INVALID_PARAMS, 'message': '分类不存在!'})
        category = categoryList.first()
        goodsInfoList = category.goodsinfo_set.all()
        if goodsInfoList.count() == 0:
            return Response({'code': HttpCode.HTTP_DATA_NULL, 'message': '此分类还未添加任何商品!'})
        else:
            return Response(
                {'code': HttpCode.HTTP_SUCCESS, 'message': "成功",
                 'data': GoodsInfoSerializes(goodsInfoList, many=True).data})
