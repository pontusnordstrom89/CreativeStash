from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import EditSocialProfile
from theStash.models import Profile

# Create your views here.

@login_required
def profile_settings(request):
    '''template = loader.get_template('stashProfile/profile_settings.html')'''
    
    return HttpResponse("Här är social_profile")


@login_required
def social_profile(request):
    template = loader.get_template('stashProfile/social_profile.html')
    
    context = {
        'Tobben': 'Vadsomhelst'
    }
    return HttpResponse(template.render(context, request))

@login_required
def edit_social_profile(request, user_profile_id):
    template = loader.get_template('stashProfile/edit_social_profile.html')

    if request.method == 'POST':
        update_form = EditSocialProfile(request.POST)

        if update_form.is_valid():

            # Return an object without saving to the DB
            form_object = update_form.save(commit=False)

            # Add an author field which will contain current user's id
            form_object.user = User.objects.get(pk=request.user.id)
            
            # Save the final "real form" to the DB
            form_object.save()
            
            return redirect('stashProfile/social_profile')
    
    else:
    
        profile = User.objects.get(pk=request.user.id)
        print(profile)
        
        # If this is a GET (or any other method) create the default form.
        form = EditSocialProfile(initial={'bio': profile.bio})
        context = {
            'form': form
        }
    
    return HttpResponse(template.render(context, request))