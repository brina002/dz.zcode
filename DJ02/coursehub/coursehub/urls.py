"""
URL configuration for coursehub project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls')),  # Подключаем URLs приложения courses
]