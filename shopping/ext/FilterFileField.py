# -*- coding: UTF-8 -*-
'''
@author: TangRen
@time: 2020/1/3
@file: FilterFileField.py
@desc: 过滤文件

'''

from django.db.models import FileField
from django.forms import forms
from django.template.defaultfilters import filesizeformat


class FilterFileField(FileField):
    def __init__(self, *args, **kwargs):
        self.content_types = kwargs.pop("content_types", [])
        self.max_upload_size = kwargs.pop("max_upload_size", [])

        super().__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super().clean(*args, **kwargs)
        file = data.file

        try:
            content_type = file.content_type
            for type in self.content_types:
                print("type="+type+",contentType="+content_type)
            if content_type in self.content_types:
                if file.size > self.max_upload_size:
                    raise forms.ValidationError('文件大小请低于 {}.当前 {}'
                                                .format(filesizeformat(self.max_upload_size),
                                                        filesizeformat(file.size)))
            else:
                raise forms.ValidationError('仅支持.apk类型')
        except AttributeError:
            pass
        return data
