# Generated by Django 2.2.4 on 2020-01-03 18:47

from django.db import migrations, models
import shopping.ext.FilterFileField


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0015_auto_20200103_1201'),
    ]

    operations = [
        migrations.CreateModel(
            name='VersionManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_code', models.SmallIntegerField(blank=True, null=True, verbose_name='版本号')),
                ('version_name', models.CharField(blank=True, max_length=25, null=True, verbose_name='版本名')),
                ('apk_file', shopping.ext.FilterFileField.FilterFileField(upload_to='apk/', verbose_name='应用程序')),
                ('force', models.BooleanField(choices=[(True, '强制更新'), (False, '手动更新')], default=False, verbose_name='更新方式')),
                ('invalid_date', models.DateField(verbose_name='有效期')),
            ],
            options={
                'verbose_name': '版本管理表',
                'verbose_name_plural': '版本管理表',
            },
        ),
    ]