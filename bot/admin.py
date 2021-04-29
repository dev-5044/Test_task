from django.contrib import admin
from bot.models import Asset


@admin.register(Asset)
class AdminAsset(admin.ModelAdmin):
    list_display = ['name', 'limit', 'quantity', 'price']
    list_editable = ['limit', 'quantity', ]
