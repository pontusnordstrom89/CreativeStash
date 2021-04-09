from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import CreateIdeaForm
from theStash.models import Idea
from django.contrib.auth.models import User

def index(request):
    latest_idea_list = Idea.objects.order_by('-idea_title')
    template = loader.get_template('stashEditor/index.html')
    context = {
        'latest_idea_list': latest_idea_list
    }
    return HttpResponse(template.render(context, request))


@login_required
def create(request):
    template = loader.get_template('stashEditor/create.html')
    form = CreateIdeaForm(request.POST or None, request.FILES or None)

   
    # create object of form
    

     # check if form data is valid
    if form.is_valid():
        # Return an object without saving to the DB
        obj = form.save(commit=False)
        # Add an author field which will contain current user's id
        obj.creator = User.objects.get(pk=request.user.id)
        obj.save()  # Save the final "real form" to the DB
        # save the form data to model
        return redirect('/')

    
    context = {
        'form': form
        }

    
    return HttpResponse(template.render(context, request))


