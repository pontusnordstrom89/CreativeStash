from django import forms

from theStash.models import Idea

class CreateIdeaForm(forms.ModelForm):

    class Meta:
        model = Idea
        fields = ['title', 'profile', 'description', 'public']
