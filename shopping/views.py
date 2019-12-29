from django.db.models import Q
from django.shortcuts import render

from rest_framework.decorators import api_view

from rest_framework.views import APIView
from rest_framework.response import Response

from shopping.response import HttpCode
from shopping.serializers.user_serializers import UserSerializers, SaveUserSerializers
from shopping.models import UserTable
import random, string,time


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
        if user_mobile is None or  not user_mobile.strip():
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
                return Response({'code': HttpCode.HTTP_INVALID_PARAMS, 'message': '用户不存在!'})
