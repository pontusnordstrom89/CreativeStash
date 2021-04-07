from django.urls import path

from . import views


urlpatterns = [
    # ex: /movies/
    path('', views.index, name='theStashindex'),
    path('restricted', views.restricted_to_users, name='restricted'),
    path('theStash/signup', views.signup, name='signup'),
    path('theStash/welcome', views.welcome, name='welcome'),
]
