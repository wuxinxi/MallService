# Generated by Django 2.2.4 on 2019-12-30 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0004_shipaddress_usertable'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardgoods',
            name='userTable',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopping.UserTable', verbose_name='用户信息'),
        ),
        migrations.AddField(
            model_name='messageinfo',
            name='userTable',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopping.UserTable', verbose_name='用户信息'),
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='userTable',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopping.UserTable', verbose_name='用户信息'),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='userTable',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopping.UserTable', verbose_name='用户信息'),
        ),
    ]