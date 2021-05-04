from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def profile_settings(request):
    '''template = loader.get_template('stashProfile/profile_settings.html')'''
    
    return HttpResponse("Här är social_profile")


@login_required
def social_profile(request):
    template = loader.get_template('stashProfile/social_profile.html')
    return HttpResponse(template.render())

# Create your views here.
