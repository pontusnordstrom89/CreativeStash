from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from .models import Idea, Category, Profile
from django.contrib.auth.models import User


def index(request):
    template = loader.get_template('theStash/index.html')

    categoy_list = Category.objects.order_by('category_name')
    latest_idea_list = Idea.objects.order_by('idea_title')[:20]

    category_name = {}
    for cat in categoy_list:
        test = cat.list_idea_categories.all()

        if test:
            category_name[cat] = [test]

        else:
            pass

    print(type(category_name))
    context = {
        'latest_idea_list': latest_idea_list,
        'category': category_name
    }
    return HttpResponse(template.render(context, request))


def detail(request, user_poth, idea_id):
    idea = get_object_or_404(Idea, pk=idea_id)
    idea_creator_profile = Profile.objects.get(user_id=user_poth)
    
    template = loader.get_template('theStash/detail.html')
    context = {
        'idea': idea,
        'profile': idea_creator_profile
    }
    return HttpResponse(template.render(context, request))



'''
Innan funktionen under (restricted_to_users) körs används en decorator = @login_required det är en inbyggd funktion vi får från django som ser om användaren är inloggad
Om användaren är inloggad körs funktionen och sidan visas, annars dirigeras användaren till Loginsidan
'''

@login_required
def restricted_to_users(request):
    template = loader.get_template('theStash/restricted.html')

    text = "The restricted area!!"
    context = {
        'restricted': text
    }
    return HttpResponse(template.render(context, request))


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
            
    else:
        form = SignUpForm()
    return render(request, 'theStash/signup.html', {'form': form})

def welcome(request):
    template = loader.get_template('theStash/welcome.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
