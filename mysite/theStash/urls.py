from django.urls import path

from . import views
from django.conf.urls import url 

app_name = 'theStash'
urlpatterns = [
    path('', views.index, name='theStashindex'),
    path('theStash/signup', views.signup, name='signup'),
    path('theStash/search_result/', views.search_result, name='search_result'),
    path('<int:user_id>/<int:idea_id>/', views.detail, name='detail'),
    path('theStash/<str:category_name>/',
         views.category_detail, name='category_detail'),
    path('most_liked', views.most_liked, name='most_liked'),
    url(r'^ajax/like_counter/$', views.like_counter, name='like_counter'),
]
