from django.urls import path, re_path
from django.conf.urls import url
from . import views


app_name = 'stashEditor'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('how_it_works', views.how_it_works, name='how_it_works'),
    url(r'^ajax/validate_categories/$',
        views.validate_categories, name='validate_categories'),
]
