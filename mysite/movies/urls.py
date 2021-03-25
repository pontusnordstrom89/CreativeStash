from django.urls import path

from . import views

urlpatterns = [
    # ex: /movies/
    path('', views.index, name='index'),
    # ex: /movies/2/
    path('<int:movie_id>/', views.detail, name='detail'),
]
