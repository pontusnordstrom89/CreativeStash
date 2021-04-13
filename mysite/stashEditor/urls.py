from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'stashEditor'
urlpatterns = [
    # ex: /movies/
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
]
