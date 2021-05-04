from django.urls import path, re_path
from django.conf.urls import url
from . import views


app_name = 'stashProfile'
urlpatterns = [
    path('profile_settings', views.profile_settings, name='profile_settings'),
    path('social_profile', views.social_profile, name= 'social_profile'),

    ]