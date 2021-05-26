from django.contrib import admin

from .models import Inventory


class InventoryDisplay(admin.ModelAdmin):
    list_display = [field.name for field in Inventory._meta.fields]
    list_per_page = 20


admin.site.register(Inventory, InventoryDisplay)
