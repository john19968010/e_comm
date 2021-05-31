from django.contrib import admin

from .models import Product


class ProductDisplay(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    list_per_page = 20


admin.site.register(Product, ProductDisplay)
