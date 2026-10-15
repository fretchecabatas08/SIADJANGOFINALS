from django.contrib import admin
from .models import LostFoundItem


@admin.register(LostFoundItem)
class LostFoundItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'item_name',
        'category',
        'lost_found_status',
        'location',
        'date_reported',
        'item_status',
        'reporter_name',
    )

    list_filter = (
        'lost_found_status',
        'item_status',
        'category',
    )

    search_fields = (
        'item_name',
        'description',
        'location',
        'reporter_name',
    )