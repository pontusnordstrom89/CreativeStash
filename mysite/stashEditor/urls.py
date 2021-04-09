from django.urls import path

from . import views


app_name = 'stashEditor'
urlpatterns = [
    # ex: /movies/
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
]
