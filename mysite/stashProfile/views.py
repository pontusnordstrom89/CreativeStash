from django.core.exceptions import ValidationError
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
    profile = get_object_or_404(Profile, user_id=user_profile_id)
   


    if request.method == 'POST' or None:
        form = EditSocialProfile(request.POST)
        profile.user = get_object_or_404(User, pk=user_profile_id)
        
        '''
        Formen validerar inte pga user inte är specificerad. 

        Något med OneToOneField som spökar. 

        Möjligt att välja flera user i form???

        elif slår ut pga Validation Error


        https://docs.djangoproject.com/en/3.2/ref/forms/validation/
        https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms
        https://stackoverflow.com/questions/27832076/modelform-with-onetoonefield-in-django
        '''
        if form.is_valid():
            
            form.save()
            return redirect('/')

        elif ValidationError:
            print('ValidationError')
            
        else:
            print('Something is wrong')
        
    else:
    
        form = EditSocialProfile(instance=profile)

        context = {
            'form': form
        }
    
        return HttpResponse(template.render(context, request))



