from django.contrib import admin

# Register your models here.

from shopping.models import UserTable, CardGoods, Category, GoodsInfo, \
    GoodsSku, MessageInfo, OrderGoods, OrderInfo, ShipAddress,GoodsBanner,VersionManager

admin.site.site_header = '商品管理系统'
admin.site.site_title = '个人商品管理系统'


class CommonAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserTable, CommonAdmin)
admin.site.register(CardGoods, CommonAdmin)
admin.site.register(Category, CommonAdmin)
admin.site.register(GoodsInfo, CommonAdmin)
admin.site.register(GoodsSku, CommonAdmin)
admin.site.register(MessageInfo, CommonAdmin)
admin.site.register(OrderGoods, CommonAdmin)
admin.site.register(OrderInfo, CommonAdmin)
admin.site.register(ShipAddress, CommonAdmin)
admin.site.register(GoodsBanner, CommonAdmin)
admin.site.register(VersionManager, CommonAdmin)
