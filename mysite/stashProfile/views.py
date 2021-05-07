from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import EditSocialProfile, EditIdeaForm
from theStash.models import Profile, Idea

# Create your views here.

@login_required
def profile_settings(request):
    '''template = loader.get_template('stashProfile/profile_settings.html')'''
    
    return HttpResponse("Här är social_profile")


@login_required
def social_profile(request):
    template = loader.get_template('stashProfile/social_profile.html')
    userID = User.objects.get(pk=request.user.id)
    categoy_list = Idea.objects.filter(creator=userID)

    context = {
        'ideas': categoy_list
    }
    return HttpResponse(template.render(context, request))


@login_required
def edit_idea(request, idea_id):
    template = loader.get_template('stashProfile/edit_idea.html')
    idea = get_object_or_404(Idea, pk=idea_id)
    form = EditIdeaForm(instance=idea)

    if request.method == 'POST':
        form = EditIdeaForm(request.POST, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('/')

        elif ValidationError:
            print('ValidationError')
        else:
            print('Something is wrong')

    context = {
        'content': form
    }
    return HttpResponse(template.render(context, request))

@login_required
def edit_social_profile(request, user_profile_id):
    template = loader.get_template('stashProfile/edit_social_profile.html')
    profile = get_object_or_404(Profile, pk=user_profile_id)
    form = EditSocialProfile(instance=profile)


    if request.method == 'POST':
        form = EditSocialProfile(request.POST, instance=profile)
       
      
        if form.is_valid():
            
            form.save()
            return redirect('/')

        elif ValidationError:
            print('ValidationError')
            
        else:
            print('Something is wrong')
  

    context = {
        'form': form
    }
    
    return HttpResponse(template.render(context, request))



