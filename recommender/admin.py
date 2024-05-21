from django.contrib import admin
from .models import ViewHistory


@admin.register(ViewHistory)
class ViewHistoryAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'product_id', 'visited_times', 'last_visited_at')
    search_fields = ('user_id', 'product_id')
