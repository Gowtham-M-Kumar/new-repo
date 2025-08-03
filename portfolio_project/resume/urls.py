from django.urls import path
from . import views

app_name = 'resume'

urlpatterns = [
    path('', views.resume_view, name='resume_view'),
    path('create/', views.resume_section_create, name='resume_section_create'),
    path('<int:pk>/edit/', views.resume_section_update, name='resume_section_update'),
    path('<int:pk>/delete/', views.resume_section_delete, name='resume_section_delete'),
    path('manage/', views.resume_manage, name='resume_manage'),
] 