from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from .models import Idea, Category, Profile
from django.contrib.auth.models import User
from django.db.models import Q
import operator


def index(request):
    template = loader.get_template('theStash/index.html')

    categoy_list = Category.objects.order_by('category_name')
    latest_idea_list = Idea.objects.order_by('idea_title')

    category_name = {}
    for cat in categoy_list:
        categories = cat.list_idea_categories.all()
        print(len(categories))
        if categories:
            category_name[cat] = [categories]
        else:
            pass

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



def search_result(request):
    template = loader.get_template('theStash/search_result.html')

    if request.method == 'GET':
        query = request.GET.get('q')
        print(query)
        if query:
            query_list = query.split()
            for q in query_list:
                result_idea = Idea.objects.filter(
                    Q(idea_title__icontains=q) | Q(idea_description__icontains=q))

                result_category = Category.objects.filter(
                    Q(category_name__icontains=q))

            search_hits = len(result_idea) + len(result_category)
            context = {
                'search_query': query,
                'search_result_idea': result_idea,
                'search_result_category': result_category,
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
            user_profile = Profile(user_id=userID.id)
            user_profile.save()
            
            return redirect('/')
            
    else:
        form = SignUpForm()
    return render(request, 'theStash/signup.html', {'form': form})

