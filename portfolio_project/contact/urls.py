from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.contact_view, name='contact_view'),
    path('edit/', views.contact_info_edit, name='contact_info_edit'),
    path('messages/', views.contact_messages, name='contact_messages'),
    path('messages/<int:pk>/', views.contact_message_detail, name='contact_message_detail'),
    path('messages/<int:pk>/delete/', views.contact_message_delete, name='contact_message_delete'),
] 