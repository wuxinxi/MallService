from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from shopping.ext.FilterFileField import FilterFileField


# Create your models here.
# 数据库


#继承Django自带的userModel类的父类。为了使用自带的Token验证系统
class UserTable(models.Model):
    """
    用户表
    """
    gender = [
        (0, '保密'),
        (1, '男'),
        (2, '女'),
    ]
    user_name = models.CharField(max_length=45, verbose_name='用户名' )
    user_pwd = models.CharField(max_length=45, verbose_name='密码')
    user_mobile = models.CharField(max_length=45, verbose_name='手机号')
    user_icon = models.ImageField(upload_to='image/user/', verbose_name='头像', null=True, blank=True)
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


# 删除数据库记录时同时删除响应的文件
@receiver(pre_delete, sender=UserTable)
def UserTable_delete_invalid(sender, instance, **kwargs):
    instance.user_icon.delete(False)


class CardGoods(models.Model):
    """
    购物车表
    """
    userTable = models.ForeignKey(UserTable, null=True, on_delete=models.CASCADE, verbose_name='用户信息')
    goods_id = models.SmallIntegerField(verbose_name='商品ID', unique=True)
    goods_desc = models.CharField(max_length=255, verbose_name='商品描述')
    goods_icon = models.CharField(max_length=255, verbose_name='商品图片')
    goods_price = models.BigIntegerField(verbose_name='商品单价')
    goods_count = models.SmallIntegerField(verbose_name='商品总数', default=0)
    goods_sku = models.CharField(max_length=255, verbose_name='商品属性')
    goods_time = models.DateTimeField(auto_now=True, verbose_name="加入购物车的时间")

    class Meta:
        verbose_name = '购物车信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.id}-{self.goods_desc}'


class Category(models.Model):
    """
    商品分类表
    """
    category_name = models.CharField(max_length=45, verbose_name="名称")
    category_content = models.CharField(max_length=255, verbose_name="分类描述", null=True, blank=True)
    category_icon = models.ImageField(upload_to='image/category/', verbose_name="分类图片", null=True, blank=True)

    class Meta:
        verbose_name = '商品分类表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.category_name}-{self.id}'


@receiver(pre_delete, sender=Category)
def Category_delete_invalid(sender, instance, **kwargs):
    instance.category_content.delete(False)


class GoodsBanner(models.Model):
    """
    商品信息轮播图
    """
    url = models.ImageField(upload_to='image/goods/', verbose_name='轮播图')

    class Meta:
        verbose_name = '商品信息轮播图表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return ("轮播图%s" % self.id)


@receiver(pre_delete, sender=GoodsBanner)
def GoodsBanner_delete_invalid(sender, instance, **kwargs):
    instance.url.delete(False)


class GoodsSku(models.Model):
    """
    商品属性表
    """
    goods_sku_title = models.CharField(max_length=45, verbose_name='商品属性标题')
    goods_sku_content = models.CharField(max_length=255, verbose_name='商品属性内容')

    class Meta:
        verbose_name = '商品属性表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods_sku_title


class GoodsInfo(models.Model):
    """
    商品信息表
    """
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, verbose_name='商品分类')
    banner = models.ManyToManyField(GoodsBanner, verbose_name='轮播图')
    sku = models.ManyToManyField(GoodsSku, verbose_name='商品属性')
    goods_desc = models.CharField(max_length=255, verbose_name='商品描述')
    goods_default_icon = models.ImageField(upload_to='image/goods/', null=True, blank=True, verbose_name='商品图片')
    goods_default_price = models.SmallIntegerField(verbose_name='商品默认单价')
    goods_detail_one = models.CharField(max_length=255, null=True, blank=True, verbose_name='商品描述1')
    goods_detail_two = models.CharField(max_length=255, null=True, blank=True, verbose_name='商品描述2')
    goods_sales_count = models.SmallIntegerField(verbose_name='已售总数', default=0)
    goods_stock_count = models.SmallIntegerField(verbose_name='库存总数', default=0)
    goods_code = models.CharField(max_length=45, verbose_name='商品代码')
    goods_default_sku = models.CharField(max_length=255, null=True, blank=True, verbose_name='默认商品属性')

    class Meta:
        verbose_name = '商品信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.goods_desc}-{self.id}'


@receiver(pre_delete, sender=GoodsInfo)
def GoodsInfo_delete_invalid(sender, instance, **kwargs):
    instance.goods_default_icon.delete(False)


class MessageInfo(models.Model):
    """
    消息表
    """
    userTable = models.ManyToManyField(UserTable, verbose_name='用户信息')
    msg_icon = models.ImageField(upload_to='image/message/', null=True, blank=True, verbose_name='消息图片')
    msg_title = models.CharField(max_length=45, verbose_name='消息标题')
    msg_content = models.CharField(max_length=255, verbose_name='消息内容')
    msg_time = models.DateTimeField(auto_now_add=True, verbose_name='消息时间')

    class Meta:
        verbose_name = '消息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.msg_title


@receiver(pre_delete, sender=MessageInfo)
def MessageInfo_delete_invalid(sender, instance, **kwargs):
    instance.msg_icon.delete(False)


class OrderGoods(models.Model):
    """
    订单商品表
    """
    userTable = models.ForeignKey(UserTable, null=True, on_delete=models.CASCADE, verbose_name='用户信息')
    goods_id = models.SmallIntegerField(verbose_name='商品ID', unique=True)
    goods_desc = models.CharField(max_length=255, verbose_name='商品描述')
    goods_icon = models.CharField(max_length=255, null=True, blank=True, verbose_name='商品图片')
    goods_price = models.SmallIntegerField(verbose_name='商品单价')
    goods_count = models.SmallIntegerField(verbose_name='商品总数')
    goods_sku = models.CharField(max_length=255, null=True, blank=True, verbose_name='默认商品属性')
    order_id = models.SmallIntegerField(verbose_name='订单Id')

    class Meta:
        verbose_name = '订单商品表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order_id


class OrderInfo(models.Model):
    """
    订单信息表
    """
    payType = [
        (0, '现金'),
        (1, '支付宝'),
        (2, '微信'),
        (3, '银联'),
    ]
    orderStatus = [
        (0, '已收货'),
        (1, '待支付'),
        (2, '待发货'),
        (3, '待收货'),
        (4, '已发货'),
        (5, '待退款'),
        (6, '已退款'),
        (10, '待更新'),
    ]
    userTable = models.ForeignKey(UserTable, null=True, on_delete=models.CASCADE, verbose_name='用户信息')
    pay_type = models.SmallIntegerField(choices=payType, default=0, verbose_name='付款方式')
    ship_id = models.SmallIntegerField(verbose_name='发货id')
    total_price = models.BigIntegerField(verbose_name='总价')
    order_status = models.SmallIntegerField(verbose_name='订单状态', default=10)

    class Meta:
        verbose_name = '订单信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ship_id


class ShipAddress(models.Model):
    """
    地址管理表
    """
    isDefaultAddress = [
        (0, '默认'),
        (1, '非默认')
    ]
    ship_user_name = models.CharField(max_length=45, verbose_name='签收名')
    ship_user_mobile = models.CharField(max_length=45, verbose_name='手机号码')
    ship_address = models.CharField(max_length=255, verbose_name='收货地址')
    ship_is_default = models.SmallIntegerField(choices=isDefaultAddress, verbose_name='是否默认', default=1)
    userTable = models.ForeignKey(UserTable, null=True, on_delete=models.CASCADE, verbose_name='用户信息')

    class Meta:
        verbose_name = '地址管理表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.id}-{self.ship_user_name}'


class VersionManager(models.Model):
    updateType = [
        (True, '强制更新'),
        (False, '手动更新'),
    ]
    version_code = models.SmallIntegerField(null=True, blank=True, verbose_name='版本号')
    version_name = models.CharField(max_length=25, null=True, blank=True, verbose_name='版本名')
    apk_file = FilterFileField(content_types=['application/vnd.android.package-archive', ], max_upload_size=5242880,
                               upload_to="apk/", verbose_name='应用程序')
    force = models.BooleanField(default=False, choices=updateType, verbose_name='更新方式')
    invalid_date = models.DateField(verbose_name='有效期')

    class Meta:
        verbose_name = '版本管理表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.id}-{self.version_name}'


@receiver(pre_delete, sender=VersionManager)
def VersionManager_delete_invalid(sender, instance, **kwargs):
    instance.apk_file.delete(False)
