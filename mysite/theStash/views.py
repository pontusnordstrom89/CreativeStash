import operator
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import SignUpForm
from .models import Idea, Category, Profile



def index(request):
    template = loader.get_template('theStash/index.html')

    if request.user.is_authenticated:
        #Get user interests
        users_interests = Profile.objects.get(
            user_id=request.user.id).user_interests.all()[:20]

        my_dict = {}

        for category_name in users_interests:
            ideas = Idea.objects.filter(idea_category__pk=category_name)

            my_dict[category_name] = ideas
        #print(type(my_dict))
        #print(type(my_dict[category_name]))
        #print(my_dict[category_name][0].creator)

    else:
        my_dict = Idea.objects.all()



    context = {
        'everything': my_dict
    }

    return HttpResponse(template.render(context, request))


def detail(request, user_id, idea_id):
    idea = get_object_or_404(Idea, pk=idea_id)
    idea_creator_profile = Profile.objects.get(user_id=user_id)
    idea_creator = User.objects.get(pk=user_id)

    template = loader.get_template('theStash/detail.html')
    context = {
        'idea': idea,
        'profile': idea_creator_profile,
        'creator': idea_creator,
    }
    return HttpResponse(template.render(context, request))

def category_detail(request, category_name):
    idea = Idea.objects.filter(idea_category=category_name)

    template = loader.get_template('theStash/category_detail.html')
    context = {
        'idea_in_category': idea,
        'category_name': category_name
    }
    return HttpResponse(template.render(context, request))


def search_result(request):
    template = loader.get_template('theStash/search_result.html')

    if request.method == 'GET':
        query = request.GET.get('q')

        if query:
            query_list = query.split()

            for q in query_list:
                result_idea = Idea.objects.filter(
                    Q(idea_title__icontains=q) | Q(idea_description__icontains=q))

                result_category = Category.objects.filter(
                    Q(category_name__icontains=q))

                result_user = User.objects.filter(
                    Q(username__icontains=q))

            search_hits = len(result_idea) + len(result_category) + len(result_user)

            if search_hits == 0:
                context = {
                    'nothing_found': 'Nothing found, let´s create something'
                }
            else:
                context = {
                    'search_query': query,
                    'search_result_idea': result_idea,
                    'search_result_category': result_category,
                    'search_result_user': result_user,
                    'search_hits': search_hits
                }

        else:
            context = {
                'nothing_found': 'Nothing found, let´s create something'
            }

    else:
        context = {
            'help': 'Try search for something'
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

            userID = User.objects.get(pk=request.user.id)
            user_profile = Profile(user_id=userID.id, bio='Welcome user, to your profile page')
            user_profile.save()

            return redirect('/')

    else:
        form = SignUpForm()
    return render(request, 'theStash/signup.html', {'form': form})
