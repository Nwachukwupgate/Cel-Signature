from django.contrib import admin
from .models import *
# Register your models here.

class TrendingProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'new_price')

class  ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

class TestimonyAdmin(admin.ModelAdmin):
    list_display = ('name', 'testimony')

class ShopAdmin(admin.ModelAdmin):
    list_display = ('description', 'new_price')

class ShopDetailsAdmin(admin.ModelAdmin):
    list_display = ('short_desc', 'full_desc')

admin.site.register(Shop, ShopAdmin)
admin.site.register(TrendingProduct, TrendingProductAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Testimony, TestimonyAdmin)
admin.site.register(ShopDetails, ShopDetailsAdmin)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Shipping)

