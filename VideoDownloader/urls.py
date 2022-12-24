from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('Downloader.urls')),
    path('admin/', admin.site.urls),
]
