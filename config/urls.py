from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Google Authentication URLs
    path('', include('googleauth.urls')),  # Google Authentication App
    path('chat/', include('chatApp.urls')),  # Chat Application
]
