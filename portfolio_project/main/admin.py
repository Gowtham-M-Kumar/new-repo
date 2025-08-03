from django.contrib import admin
from .models import Contact, Project, ResumeSection, AboutContent, ContactInfo, Settings

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['created_at']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description', 'tags']
    list_editable = ['order', 'is_active']
    prepopulated_fields = {'tags': ('title',)}

@admin.register(ResumeSection)
class ResumeSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'section_type', 'order', 'is_active']
    list_filter = ['section_type', 'is_active']
    search_fields = ['title', 'subtitle', 'description']
    list_editable = ['order', 'is_active']

@admin.register(AboutContent)
class AboutContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated_at']
    search_fields = ['title', 'content', 'skills']

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['email', 'updated_at']
    search_fields = ['email']

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['updated_at']
    readonly_fields = ['updated_at']
    
    def has_add_permission(self, request):
        # Only allow one settings instance
        return not Settings.objects.exists()
