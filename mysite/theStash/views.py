from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required



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


