from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from theStash.models import Profile, Idea
from .forms import EditSocialProfile, EditIdeaForm

@login_required
def profile_settings(request):
    '''template = loader.get_template('stashProfile/profile_settings.html')'''

    return HttpResponse("Här är social_profile")


@login_required
def social_profile(request, user_profile_id):
    template = loader.get_template('stashProfile/social_profile.html')
    #userID = User.objects.get(pk=request.user.id)
    profile = get_object_or_404(Profile, user_id=user_profile_id)
    user = get_object_or_404(User, id=user_profile_id)
    idea_list = Idea.objects.filter(creator=user_profile_id)
    users_interests = Profile.objects.get(user_id=user_profile_id).user_interests.all()

    context = {
        'ideas': idea_list,
        'profile': profile,
        'show_user': user,
        'user_interests': users_interests
    }
    return HttpResponse(template.render(context, request))


@login_required
def edit_idea(request, idea_id):
    template = loader.get_template('stashProfile/edit_idea.html')
    idea = get_object_or_404(Idea, pk=idea_id)
    form = EditIdeaForm(instance=idea)
    userID = User.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = EditIdeaForm(request.POST, instance=idea)

        if form.is_valid():
            form.save()
            return redirect(f'/{userID.id}/{idea_id}')

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
    profile = get_object_or_404(Profile, user_id=user_profile_id)
    #form = EditSocialProfile(instance=profile)
    fs = FileSystemStorage()

    if request.method == 'POST':
        form = EditSocialProfile(request.POST, request.FILES, instance=profile)

        # check if form data is valid
        if form.is_valid():
            profile_picture = request.FILES.get('profile_picture')
            form_object = form.save(commit=False)

            if profile_picture:
                #Save the uploaded image
                name = fs.save(profile_picture.name, profile_picture)
                url = fs.url(name)
                form_object.image = url

            else:
                form_object.image = '/media/profilepics/default_profile.png'

            #Save the form to database
            form.save()
            #Redirect to user profile
            return redirect(f'/stashProfile/social_profile/{user_profile_id}')

    else:
        form = EditSocialProfile(instance=profile)


    context = {
        'form': form
    }

    return HttpResponse(template.render(context, request))

