from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import SignUpForm



def index(request):
    template = loader.get_template('theStash/index.html')
    context = {
        'CreativeStash': 'CreativeStash'
    }
    return HttpResponse(template.render(context, request))


'''

Innan funktionen under (restricted_to_users) körs används en decorator = @login_required det är en inbyggd funktion vi får från django som ser om användaren är innloggad
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
            return redirect('welcome')
            
    else:
        form = SignUpForm()
    return render(request, 'theStash/signup.html', {'form': form})

def welcome(request):
    template = loader.get_template('theStash/welcome.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
