from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import CreateIdeaForm
from theStash.models import Idea


def index(request):
    latest_idea_list = Idea.objects.order_by('-title')[:5]
    template = loader.get_template('stashEditor/index.html')
    context = {
        'latest_idea_list': latest_idea_list
    }
    return HttpResponse(template.render(context, request))


@login_required
def create(request):
    template = loader.get_template('stashEditor/create.html')

    
    # create object of form
    form = CreateIdeaForm(request.POST or None, request.FILES or None)

     # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        return redirect('/')

    
    context = {
        'form': form
        }

    
    return HttpResponse(template.render(context, request))


