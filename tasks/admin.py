from django.contrib import admin
from .models import Task

@admin.register(Task)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'created_at')
    list_filter = ('status', 'project')
    search_fields = ('title', 'description')
    list_editable = ('status',)
