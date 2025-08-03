from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description', 'tags']
    list_editable = ['order', 'is_active']
    prepopulated_fields = {'tags': ('title',)}
    readonly_fields = ['created_at', 'updated_at']
