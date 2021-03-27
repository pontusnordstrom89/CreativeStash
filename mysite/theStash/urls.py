from django.urls import path

from . import views

urlpatterns = [
    # ex: /movies/
    path('', views.index, name='index'),
    path('restricted', views.restricted_to_users, name='restricted'),
]
