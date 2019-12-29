from django.contrib import admin

# Register your models here.

from shopping.models import UserTable

admin.site.site_header = '商品管理系统'
admin.site.site_title = '个人商品管理系统'


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserTable, UserAdmin)
