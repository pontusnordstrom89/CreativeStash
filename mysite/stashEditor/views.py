from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from theStash.models import Idea, Category
from .forms import CreateIdeaForm, CreateCategoryFrom


list_of_categories = []

def validate_categories(request):
    category_name = request.GET.get('category_name', None)
    data = {
        'is_taken': Category.objects.filter(category_name__iexact=category_name).exists()
    }

    global list_of_categories
    list_of_categories.append(category_name)

    if data['is_taken']:
        data['category'] = category_name
    else:
        data['category'] = category_name
        new_category = Category(category_name=category_name)
        new_category.save()

    return JsonResponse(data)



@login_required
def create(request):
    template = loader.get_template('stashEditor/create.html')
    fs = FileSystemStorage()

    if request.method == 'POST':
        global list_of_categories
        create_idea_form = CreateIdeaForm(request.POST)

        # check if form data is valid
        if create_idea_form.is_valid():
            uploaded_picture = request.FILES.get('image')
            # Return an object without saving to the DB
            form_object = create_idea_form.save(commit=False)

            # Add an author field which will contain current user's id
            form_object.creator = User.objects.get(pk=request.user.id)


            if uploaded_picture:
                #Save the uploaded image
                name = fs.save(f"upload-{uploaded_picture.name}", uploaded_picture)
                url = fs.url(name)
                form_object.image = url

            else:
                form_object.image = '/media/default_idea.jpg'

            # Save the final "real form" to the DB
            form_object.save()

            for item in list_of_categories:
                form_object.idea_category.add(item)

            list_of_categories = []

            return redirect(f'/{form_object.creator.id}/{form_object.id}')



    else:

        create_idea_form = CreateIdeaForm()

        context = {
            'ideaform': create_idea_form
            }

        return HttpResponse(template.render(context, request))


def how_it_works(request):
    template = loader.get_template('stashEditor/how_it_works.html')
    context = {
        }
    return HttpResponse(template.render(context, request))


