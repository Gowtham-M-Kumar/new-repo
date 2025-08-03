from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('base/', views.base, name='base'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # These URLs are now handled by their respective apps
    # path('projects/', lambda request: redirect('projects:project_list'), name='projects'),
    # path('resume/', lambda request: redirect('resume:resume_view'), name='resume'),
    # path('contact/', lambda request: redirect('contact:contact_view'), name='contact'),
    
    # Settings URLs
    path('settings/', views.settings_login, name='settings_login'),
    path('settings/dashboard/', views.settings_dashboard, name='settings_dashboard'),
    path('settings/logout/', views.settings_logout, name='settings_logout'),
    
    # About Content Management
    path('settings/about/edit/', views.edit_about, name='edit_about'),
]