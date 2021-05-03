from django.urls import path

from . import views

app_name = 'theStash'
urlpatterns = [
    # ex: /movies/
    path('', views.index, name='theStashindex'),
    path('theStash/signup', views.signup, name='signup'),
    path('theStash/search_result', views.search_result, name='search_result'),
    path('<int:user_poth>/<int:idea_id>/', views.detail, name='detail'),
]
