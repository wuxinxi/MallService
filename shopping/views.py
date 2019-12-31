from django.db.models import Q
from django.shortcuts import render

from rest_framework.decorators import api_view

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

from shopping.response import HttpCode
from shopping.serializers.user_serializers import UserSerializers, SaveUserSerializers
from shopping.serializers.message_serializers import MessageSerializers
from shopping.serializers.card_goods_serializes import CardGoodsSerializers
from shopping.serializers.category_serializers import CategorySerializers
from shopping.serializers.goods_info_serializes import GoodsInfoSerializes
from shopping.serializers.address_serializers import ShipAddressSerializers
from shopping.models import UserTable, MessageInfo, CardGoods, Category, GoodsInfo, ShipAddress
import random, string, time
import traceback
import json

from urllib import parse


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
            return Response({'code': HttpCode.HTTP_INVALID_PARAMS, 'message': '用户不存在!'})


class CardGood(APIView):
    """
    获取购物车列表接口
    """

    def get(self, request):
        params = request.data
        user_mobile = params.get('user_mobile')
        if user_mobile is None or not user_mobile.strip():
            return Response({'code': HttpCode.HTTP_INVALID_PARAMS, 'message': '参数缺省!'})
        try:
            user = UserTable.objects.get(user_mobile=user_mobile)
            goods_list = user.cardgoods_set.all()
            if goods_list.count() == 0:
                return Response({'code': HttpCode.HTTP_DATA_NULL, 'message': '还未添加任何商品到购物车!'})
            else:
                return Response(
                    {'code': HttpCode.HTTP_SUCCESS, 'message': '成功',
                     'data': CardGoodsSerializers(goods_list, many=True).data})
        except:
            return Response({'code': HttpCode.HTTP_INVALID_PARAMS, 'message': '用户不存在!'})


class CardGoodsManager(APIView):
    """
    加入购物车
    """

    def post(self, request, format=None):
        params = request.data
        user_mobile = params.get('user_mobile')
        if user_mobile is None or not user_mobile.strip():
            return Response({'code': HttpCode.HTTP_INVALID_PARAMS, 'message': '参数缺省!'})
        res = UserTable.objects.filter(user_mobile=user_mobile)
        if res.count() == 0:
            return Response({'code': HttpCode.HTTP_INVALID_PARAMS, 'message': '用户不存在!'})
        try:
            goods_id = params.get('goods_id')
            goods_desc = parse.unquote(params.get('goods_desc'))
            goods_icon = params.get('goods_icon')
            goods_price = params.get('goods_price')
            goods_count = params.get('goods_count')
            goods_sku = params.get('goods_sku')

            card_goods = CardGoods(goods_id=goods_id, goods_desc=goods_desc, goods_icon=goods_icon,
                                   goods_price=goods_price, goods_count=goods_count, goods_sku=goods_sku)
            user = res.first()
            card_goods.userTable = user
            db_card_goods = CardGoods.objects.filter(goods_id=goods_id).first()
            message = '保存成功'
            if db_card_goods is None:
                '新增'
                card_goods.save()
            else:
                '修改'
                message = '修改成功'
                card_goods.id = db_card_goods.id
                card_goods.save(force_update=True)
            return Response(
                {'code': HttpCode.HTTP_SUCCESS, 'message': message,
                 'data': CardGoodsSerializers(card_goods).data}, content_type='application/json;charset-utf-8')
        except Exception as e:
            return Response({'code': HttpCode.HTTP_EX, 'message': ('%s') % e.args},
                            content_type='application/json;charset-utf-8')

    def delete(self, request):
        """
        删除购物车
        :param request:
        :return:
        """
        params = request.data
        user_mobile = params.get('user_mobile')
        ids = params.get('ids')
        ids_str_list = ','.join([str(x) for x in ids])

        print(ids_str_list)
        if user_mobile is None or ids is None:
            return Response({'code': HttpCode.HTTP_INVALID_PARAMS, 'message': '参数缺省!'})
        try:
            user = UserTable.objects.get(user_mobile=user_mobile)
            result = user.cardgoods_set.extra(where=['id IN ( ' + ids_str_list + ' )']).delete()
            message = f'删除【{ result[0]}】条成功' if result[0] != 0 else '信息不存在!'
            code = HttpCode.HTTP_SUCCESS if result[0] != 0 else HttpCode.HTTP_DATA_NULL
            return Response({'code': code, 'message': message, 'data': message})
        except Exception as e:
            return Response({'code': HttpCode.HTTP_EX, 'message': ('%s') % e.args})


class CategoryList(APIView):
    """
    分类列表
    """

    def get(self, request):
        category_list = Category.objects.all()
        if category_list.count() == 0:
            return Response({'code': HttpCode.HTTP_DATA_NULL, 'message': '还未添加任何商品分类!'})
        else:
            return Response(
                {'code': HttpCode.HTTP_SUCCESS, 'message': "成功",
                 'data': CategorySerializers(category_list, many=True).data})


class GoodInfoList(APIView):
    """
    商品列表
    """

    def get(self, request):
        params = request.data
        category_id = params.get('id')
        if category_id is None or not category_id.strip():
            return Response({'code': HttpCode.HTTP_INVALID_PARAMS, 'message': '参数缺省!'})
        categoryList = Category.objects.filter(id=category_id)
        if categoryList.count() == 0:
            return Response({'code': HttpCode.HTTP_INVALID_PARAMS, 'message': '分类不存在!'})
        category = categoryList.first()
        goods_info_list = category.goodsinfo_set.all()
        if goods_info_list.count() == 0:
            return Response({'code': HttpCode.HTTP_DATA_NULL, 'message': '此分类还未添加任何商品!'})
        else:
            return Response(
                {'code': HttpCode.HTTP_SUCCESS, 'message': "成功",
                 'data': GoodsInfoSerializes(goods_info_list, many=True).data})


class ShipAddressList(APIView):
    """
    获取地址信息
    """

    def get(self, request):
        params = request.data
        user_mobile = params.get('user_mobile')
        if user_mobile is None or not user_mobile.strip():
            return Response({'code': HttpCode.HTTP_INVALID_PARAMS, 'message': '参数缺省!'})
        try:
            user = UserTable.objects.get(user_mobile=user_mobile)
            address_list = user.shipaddress_set.all()
            if address_list.count() == 0:
                return Response({'code': HttpCode.HTTP_DATA_NULL, 'message': '还未添加任何地址信息!'})
            else:
                return Response(
                    {'code': HttpCode.HTTP_SUCCESS, 'message': '成功',
                     'data': ShipAddressSerializers(address_list, many=True).data})
        except Exception as e:
            return Response({'code': HttpCode.HTTP_EX, 'message': ('%s') % e.args})


class ShipAddressManage(APIView):
    """
    新增或修改地址
    """

    def post(self, request):
        params = request.data
        user_mobile = params.get('user_mobile')
        if user_mobile is None or not user_mobile.strip():
            return Response({'code': HttpCode.HTTP_INVALID_PARAMS, 'message': '参数缺省!'})
        res = UserTable.objects.filter(user_mobile=user_mobile)
        if res.count() == 0:
            return Response({'code': HttpCode.HTTP_INVALID_PARAMS, 'message': '用户不存在!'})
        try:
            ship_user_name = parse.unquote(params.get('ship_user_name'))
            ship_user_mobile = params.get('ship_user_mobile')
            ship_address = parse.unquote(params.get('ship_address'))
            ship_is_default = int(params.get('ship_is_default'))
            ship_address = ShipAddress(ship_user_name=ship_user_name, ship_user_mobile=ship_user_mobile,
                                       ship_address=ship_address, ship_is_default=ship_is_default)
            message = '新增成功'
            ship_address.userTable = res.first()
            ship_id = params.get('id')
            if ship_id is None:
                '新增'
                if ship_is_default == 0:
                    ShipAddress.objects.filter(ship_is_default=0).update(ship_is_default=1)

                ship_address.save()
            else:
                '修改'
                db_address = ShipAddress.objects.filter(id=ship_id).first()
                if db_address is None:
                    '已被服务端删除'
                    if ship_is_default == 0:
                        ShipAddress.objects.filter(ship_is_default=0).update(ship_is_default=1)

                    ship_address.save()
                else:
                    message = '修改成功'
                    print(ship_is_default)
                    if ship_is_default == 0:
                        print('修改当前为默认')
                        ShipAddress.objects.filter(ship_is_default=0).update(ship_is_default=1)

                    ship_address.id = db_address.id
                    ship_address.save(force_update=True)
            return Response(
                {'code': HttpCode.HTTP_SUCCESS, 'message': message,
                 'data': ShipAddressSerializers(ship_address).data})
        except Exception as e:
            return Response({'code': HttpCode.HTTP_EX, 'message': ('%s') % e.args})

    def delete(self, request):
        """
        删除收货地址
        :param request:
        :return:
        """
        params = request.data
        user_mobile = params.get('user_mobile')
        ship_id = params.get('id')
        if user_mobile is None or ship_id is None:
            return Response({'code': HttpCode.HTTP_INVALID_PARAMS, 'message': '参数缺省!'})
        try:
            user = UserTable.objects.get(user_mobile=user_mobile)
            result = user.shipaddress_set.filter(id=ship_id).delete()
            message = '删除成功' if result[0] == 1 else '信息不存在!'
            code = HttpCode.HTTP_SUCCESS if result[0] == 1 else HttpCode.HTTP_DATA_NULL
            return Response({'code': code, 'message': message, 'data': message})
        except Exception as e:
            return Response({'code': HttpCode.HTTP_EX, 'message': ('%s') % e.args})
