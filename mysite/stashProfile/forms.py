from django import forms
from theStash.models import Profile, Idea

class EditSocialProfile(forms.ModelForm):
    class Meta:
        model= Profile
        exclude = ['user']


class EditIdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        exclude = ['creator']
