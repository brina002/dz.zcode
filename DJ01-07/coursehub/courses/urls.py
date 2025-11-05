"""
URL configuration for courses app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data/', views.data_page, name='data'),
    path('test/', views.test_page, name='test'),
]