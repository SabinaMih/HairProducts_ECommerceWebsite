from django.contrib import admin
from .models import Category, Product, Review, Voucher

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'category', 'stock', 'available', 'created', 'updated', 'count_sold', 'slug']
    populated_fields = {'slug': ('title', )}
    list_editable = ['price', 'stock', 'available']
    list_per_page = 20


class VoucherAdmin(admin.ModelAdmin):
    list_display = ['code', 'valid_from', 'valid_to', 'discount', 'active']
    list_filter = ['active', 'valid_from', 'valid_to', 'category']
    search_fields = ['code']


admin.site.register(Voucher, VoucherAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review)
