# Generated by Django 2.2.4 on 2019-12-30 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0009_remove_cardgoods_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardgoods',
            name='goods_time',
            field=models.DateTimeField(auto_now=True, verbose_name='加入购物车的时间'),
        ),
    ]