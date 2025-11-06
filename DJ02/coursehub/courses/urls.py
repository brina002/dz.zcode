"""
URL configuration for courses app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('about/', views.about, name='about'),
    path('data/', views.data_page, name='data'),
    path('test/', views.test_page, name='test'),  # для совместимости
]