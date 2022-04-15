from django.contrib import admin
from .models import *


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ("date", "title", "quantity", "distance",)
    list_display_links = ("date", "title",)
    list_filter = ("date",)
    search_fields = ("date", "title",)
    list_editable = ("quantity", "distance",)