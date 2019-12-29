from django.db import models


# Create your models here.
# 数据库


class UserTable(models.Model):
    """
    用户表
    """
    gender = [
        (0, '保密'),
        (1, '男'),
        (2, '女'),
    ]
    user_name = models.CharField(max_length=45, verbose_name='用户名', )
    user_pwd = models.CharField(max_length=45, verbose_name='密码')
    user_mobile = models.CharField(max_length=45, verbose_name='手机号')
    user_icon = models.CharField(max_length=45, verbose_name='头像', null=True, blank=True)
    user_real_name = models.CharField(max_length=45, verbose_name='真实姓名', null=True, blank=True)
    user_identity_card = models.CharField(max_length=45, verbose_name='身份证', null=True, blank=True)
    user_nick_name = models.CharField(max_length=45, verbose_name='昵称', null=True, blank=True)
    user_gender = models.SmallIntegerField(verbose_name='性别', choices=gender, default=0)
    user_birthday = models.CharField(max_length=45, verbose_name='生日', null=True, blank=True)
    user_address = models.CharField(max_length=45, verbose_name='居住地', null=True, blank=True)
    user_sign = models.CharField(max_length=45, verbose_name='个性签名', null=True, blank=True)
    register_time = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '用户信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_name
