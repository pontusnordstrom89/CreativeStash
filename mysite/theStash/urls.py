from django.urls import path

from . import views

app_name = 'theStash'
urlpatterns = [
    path('', views.index, name='theStashindex'),
    path('theStash/signup', views.signup, name='signup'),
    path('theStash/search_result/', views.search_result, name='search_result'),
    path('<int:user_id>/<int:idea_id>/', views.detail, name='detail'),
    path('theStash/<str:category_name>/',
         views.category_detail, name='category_detail'),
]
