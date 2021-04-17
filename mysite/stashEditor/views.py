from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import CreateIdeaForm, CreateCategoryFrom
from theStash.models import Idea, Category
from django.contrib.auth.models import User
from django.http import JsonResponse

def index(request):
    latest_idea_list = Idea.objects.order_by('idea_title')
    template = loader.get_template('stashEditor/index.html')
    context = {
        'latest_idea_list': latest_idea_list
    }
    return HttpResponse(template.render(context, request))


def validate_categories(request):
    category_name = request.GET.get('category_name', None)
    data = {
        'is_taken': Category.objects.filter(category_name__iexact=category_name).exists()
    }

    if data['is_taken']:
        data['message'] = category_name
    else: 
        data['category'] = category_name
        new_category = Category(category_name=category_name)
        new_category.save()
        
    return JsonResponse(data)


    
@login_required
def create(request):
    template = loader.get_template('stashEditor/create.html')

    if request.method == 'POST':
        create_category_form = CreateCategoryFrom(request.POST)
        create_idea_form = CreateIdeaForm(request.POST)

        # check if form data is valid
        if create_idea_form.is_valid():
            # Return an object without saving to the DB
            form_object = create_idea_form.save(commit=False)
            # Add an author field which will contain current user's id
            form_object.creator = User.objects.get(pk=request.user.id)
            # Save the final "real form" to the DB
            form_object.save()
            
            return redirect('/')

    else:
        create_category_form = CreateCategoryFrom()
        create_idea_form = CreateIdeaForm()
    
        context = {
            'ideaform': create_idea_form,
            'categoryform': create_category_form
            }

        return HttpResponse(template.render(context, request))


def how_it_works(request):
    template = loader.get_template('stashEditor/how_it_works.html')
    return HttpResponse(template.render())
