# Generated by Django 2.2.3 on 2019-12-28 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usertable',
            options={'verbose_name': '用户信息表', 'verbose_name_plural': '用户信息表'},
        ),
        migrations.AlterField(
            model_name='usertable',
            name='register_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='注册时间'),
        ),
        migrations.AlterField(
            model_name='usertable',
            name='user_address',
            field=models.CharField(blank=True, max_length=45, null=True, verbose_name='居住地'),
        ),
        migrations.AlterField(
            model_name='usertable',
            name='user_birthday',
            field=models.CharField(blank=True, max_length=45, null=True, verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='usertable',
            name='user_gender',
            field=models.SmallIntegerField(choices=[(0, '保密'), (1, '男'), (2, '女')], default=0, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='usertable',
            name='user_icon',
            field=models.CharField(blank=True, max_length=45, null=True, verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='usertable',
            name='user_identity_card',
            field=models.CharField(blank=True, max_length=45, null=True, verbose_name='身份证'),
        ),
        migrations.AlterField(
            model_name='usertable',
            name='user_nick_name',
            field=models.CharField(blank=True, max_length=45, null=True, verbose_name='昵称'),
        ),
        migrations.AlterField(
            model_name='usertable',
            name='user_real_name',
            field=models.CharField(blank=True, max_length=45, null=True, verbose_name='真实姓名'),
        ),
        migrations.AlterField(
            model_name='usertable',
            name='user_sign',
            field=models.CharField(blank=True, max_length=45, null=True, verbose_name='个性签名'),
        ),
    ]