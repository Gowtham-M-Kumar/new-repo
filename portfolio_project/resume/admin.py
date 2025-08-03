from django.contrib import admin
from .models import ResumeSection

@admin.register(ResumeSection)
class ResumeSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'section_type', 'order', 'is_active']
    list_filter = ['section_type', 'is_active']
    search_fields = ['title', 'subtitle', 'description']
    list_editable = ['order', 'is_active']
    readonly_fields = ['created_at', 'updated_at']
