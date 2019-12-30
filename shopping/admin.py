from django.contrib import admin

# Register your models here.

from shopping.models import UserTable, CardGoods, Category, GoodsInfo, \
    GoodsSku, MessageInfo, OrderGoods, OrderInfo, ShipAddress,GoodsBanner

admin.site.site_header = '商品管理系统'
admin.site.site_title = '个人商品管理系统'


class UserAdmin(admin.ModelAdmin):
    pass


class CardGoodsAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class GoodsInfoAdmin(admin.ModelAdmin):
    pass


class GoodsSkuAdmin(admin.ModelAdmin):
    pass


class MessageInfoAdmin(admin.ModelAdmin):
    pass


class OrderGoodsAdmin(admin.ModelAdmin):
    pass


class OrderInfoAdmin(admin.ModelAdmin):
    pass


class ShipAddressAdmin(admin.ModelAdmin):
    pass


class BannerAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserTable, UserAdmin)
admin.site.register(CardGoods, CardGoodsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)
admin.site.register(GoodsSku, GoodsSkuAdmin)
admin.site.register(MessageInfo, MessageInfoAdmin)
admin.site.register(OrderGoods, OrderGoodsAdmin)
admin.site.register(OrderInfo, OrderInfoAdmin)
admin.site.register(ShipAddress, ShipAddressAdmin)
admin.site.register(GoodsBanner, BannerAdmin)
