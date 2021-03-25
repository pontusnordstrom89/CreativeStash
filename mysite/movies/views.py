from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Movie, Genre


def index(request):
    latest_movie_list = Movie.objects.order_by('release_date')[:10]
    template = loader.get_template('movies/index.html')
    context = {
        'latest_movie_list': latest_movie_list
    }
    return HttpResponse(template.render(context, request))


def detail(request, movie_id):
    movie_details = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie_details': movie_details})
