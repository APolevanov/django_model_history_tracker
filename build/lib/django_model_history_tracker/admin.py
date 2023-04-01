from django.contrib import admin
from .models import History

class HistoryAdmin(admin.ModelAdmin):
    list_display = ('action', 'content_type', 'object_id', 'timestamp', 'changes')
    list_filter = ('action', 'content_type', 'timestamp')
    search_fields = ('object_id',)

admin.site.register(History, HistoryAdmin)
