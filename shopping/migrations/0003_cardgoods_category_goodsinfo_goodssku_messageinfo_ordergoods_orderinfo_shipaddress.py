# Generated by Django 2.2.4 on 2019-12-30 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_auto_20191228_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_id', models.SmallIntegerField(unique=True, verbose_name='商品ID')),
                ('goods_desc', models.CharField(max_length=255, verbose_name='商品描述')),
                ('goods_icon', models.CharField(max_length=255, verbose_name='商品图片')),
                ('goods_price', models.BigIntegerField(verbose_name='商品单价')),
                ('goods_count', models.SmallIntegerField(default=0, verbose_name='商品总数')),
                ('user_id', models.CharField(max_length=45, verbose_name='用户ID（手机号）')),
                ('goods_sku', models.CharField(max_length=255, verbose_name='商品属性')),
                ('goods_time', models.DateTimeField(auto_now_add=True, verbose_name='加入购物车的时间')),
            ],
            options={
                'verbose_name': '购物车信息表',
                'verbose_name_plural': '购物车信息表',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=45, verbose_name='名称')),
                ('category_icon', models.CharField(blank=True, max_length=255, null=True, verbose_name='分类图片')),
                ('parent_id', models.SmallIntegerField(default=0, verbose_name='分类ID')),
            ],
            options={
                'verbose_name': '商品分类表表',
                'verbose_name_plural': '商品分类表表',
            },
        ),
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.SmallIntegerField(default=0, verbose_name='分类ID')),
                ('goods_desc', models.CharField(max_length=255, verbose_name='商品描述')),
                ('goods_default_icon', models.CharField(blank=True, max_length=255, null=True, verbose_name='商品图片')),
                ('goods_default_price', models.SmallIntegerField(verbose_name='商品默认单价')),
                ('goods_banner', models.TextField(blank=True, null=True, verbose_name='商品图')),
                ('goods_detail_one', models.CharField(blank=True, max_length=255, null=True, verbose_name='商品描述1')),
                ('goods_detail_two', models.CharField(blank=True, max_length=255, null=True, verbose_name='商品描述2')),
                ('goods_sales_count', models.SmallIntegerField(default=0, verbose_name='已售总数')),
                ('goods_stock_count', models.SmallIntegerField(default=0, verbose_name='库存总数')),
                ('goods_code', models.CharField(max_length=45, verbose_name='商品代码')),
                ('goods_default_sku', models.CharField(blank=True, max_length=255, null=True, verbose_name='默认商品属性')),
            ],
            options={
                'verbose_name': '商品信息表',
                'verbose_name_plural': '商品信息表',
            },
        ),
        migrations.CreateModel(
            name='GoodsSku',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_id', models.SmallIntegerField(unique=True, verbose_name='商品ID')),
                ('goods_sku_title', models.CharField(max_length=45, verbose_name='商品属性标题')),
                ('goods_sku_content', models.CharField(max_length=255, verbose_name='商品属性内容')),
            ],
            options={
                'verbose_name': '商品属性表',
                'verbose_name_plural': '商品属性表',
            },
        ),
        migrations.CreateModel(
            name='MessageInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_icon', models.CharField(blank=True, max_length=255, null=True, verbose_name='消息图片')),
                ('msg_title', models.CharField(max_length=45, verbose_name='消息标题')),
                ('msg_content', models.CharField(max_length=255, verbose_name='消息内容')),
                ('msg_time', models.DateTimeField(auto_now_add=True, verbose_name='消息时间')),
                ('user_id', models.CharField(max_length=45, verbose_name='用户ID（手机号）')),
            ],
            options={
                'verbose_name': '消息表',
                'verbose_name_plural': '消息表',
            },
        ),
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_id', models.SmallIntegerField(unique=True, verbose_name='商品ID')),
                ('goods_desc', models.CharField(max_length=255, verbose_name='商品描述')),
                ('goods_icon', models.CharField(blank=True, max_length=255, null=True, verbose_name='商品图片')),
                ('goods_price', models.SmallIntegerField(verbose_name='商品单价')),
                ('goods_count', models.SmallIntegerField(verbose_name='商品总数')),
                ('goods_sku', models.CharField(blank=True, max_length=255, null=True, verbose_name='默认商品属性')),
                ('order_id', models.SmallIntegerField(verbose_name='订单Id')),
            ],
            options={
                'verbose_name': '订单商品表',
                'verbose_name_plural': '订单商品表',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=45, verbose_name='用户ID（手机号）')),
                ('pay_type', models.SmallIntegerField(choices=[(0, '现金'), (1, '支付宝'), (2, '微信'), (3, '银联')], default=0, verbose_name='付款方式')),
                ('ship_id', models.BigIntegerField(max_length=11, verbose_name='发货id')),
                ('total_price', models.BigIntegerField(max_length=11, verbose_name='总价')),
                ('order_status', models.SmallIntegerField(default=10, verbose_name='订单状态')),
            ],
            options={
                'verbose_name': '订单信息表',
                'verbose_name_plural': '订单信息表',
            },
        ),
        migrations.CreateModel(
            name='ShipAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ship_user_name', models.CharField(max_length=45, verbose_name='签收名')),
                ('ship_user_mobile', models.CharField(max_length=45, verbose_name='手机号码')),
                ('ship_address', models.CharField(max_length=255, verbose_name='收货地址')),
                ('ship_is_default', models.SmallIntegerField(choices=[(0, '默认'), (1, '非默认')], default=1, verbose_name='收货地址')),
                ('user_id', models.CharField(max_length=45, verbose_name='用户ID（手机号）')),
            ],
            options={
                'verbose_name': '地址管理表',
                'verbose_name_plural': '地址管理表',
            },
        ),
    ]
