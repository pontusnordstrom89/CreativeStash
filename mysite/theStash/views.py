from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader




def index(request):
    template = loader.get_template('theStash/index.html')
    context = {
        'latest_movie_list': 'CreativeStash'
    }
    return HttpResponse(template.render(context, request))
