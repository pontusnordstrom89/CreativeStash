import operator
from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import SignUpForm, CommentForm
from .models import Idea, Category, Profile, Comments, Like




def index(request):
    template = loader.get_template('theStash/index.html')
    
    info = ""
    if request.user.is_authenticated:
        #Get user interests
        users_interests = Profile.objects.get(
            user_id=request.user.id).user_interests.all()[:20]

        my_dict = {}
    
        for category_name in users_interests:
            ideas = Idea.objects.filter(idea_category__pk=category_name)
            if len(ideas) == 0:
                pass
            else:
                my_dict[category_name] = ideas

        if my_dict == {}:
            info = 'Info text'

    else:
        my_dict = Idea.objects.all()
        

    context = {
        'everything': my_dict,
        'info': info
    }

    return HttpResponse(template.render(context, request))


def detail(request, user_id, idea_id):
    idea = get_object_or_404(Idea, pk=idea_id)
    idea_creator_profile = Profile.objects.get(user_id=user_id)
    idea_creator = User.objects.get(pk=user_id)
    comments = Comments.objects.filter(idea=idea_id)

    template = loader.get_template('theStash/detail.html')


    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet          
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.from_user = request.user
            new_comment.idea_id = idea_id
            # Save the comment to the database
            new_comment.save()
            return redirect(f'/{user_id}/{idea_id}')
    else:
        comment_form = CommentForm()

    context = {
        'idea': idea,
        'profile': idea_creator_profile,
        'creator': idea_creator,
        'comments': comments,
        'comment_form': comment_form
    }
    return HttpResponse(template.render(context, request))

def category_detail(request, category_name):
    idea = Idea.objects.filter(idea_category=category_name)

    template = loader.get_template('theStash/category_detail.html')
    context = {
        'ideas': idea,
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

 
def like_counter(request):
    idea_id = request.GET.get('idea_id', None)
    try: 
        like_idea = Like.objects.get(idea_id=idea_id)
        like_idea.idea_like += 1
        like_idea.save()
    except:
        idea = Idea.objects.get(id=idea_id)
        like_idea = Like(idea=idea, idea_like = 1)
        like_idea.save()
    data = {'message': like_idea.idea_like}
    return JsonResponse(data)

def most_liked(request):
    template = loader.get_template('theStash/most_liked.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

def like_comment(request):
    comment_id = request.GET.get('like_comment', None)
    
    
    likes = Comments.objects.get(id=comment_id)
    if likes.comment_likes == None:
        likes.comment_likes = 1

    else:
        likes.comment_likes += 1
    likes.save()

    
    data = {'message':likes.comment_likes}
    return JsonResponse(data)

