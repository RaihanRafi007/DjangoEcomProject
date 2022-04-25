from django.contrib import admin
from App_Shop.models import Category, Product

# Register your models here.

"""
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
"""

admin.site.register(Category)
admin.site.register(Product)

