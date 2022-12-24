from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('youtube', views.youtube, name="youtube"),
    path('instagram', views.instagram, name="instagram"),
    path('twitter', views.twitter, name="twitter"),
]