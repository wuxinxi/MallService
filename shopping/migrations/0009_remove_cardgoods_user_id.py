# Generated by Django 2.2.4 on 2019-12-30 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0008_auto_20191230_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardgoods',
            name='user_id',
        ),
    ]