from django import forms
from theStash.models import Profile, Idea

class EditSocialProfile(forms.ModelForm):
    class Meta:
        model= Profile
        fields = ('bio', 'link1', 'link2', 'link3', 'profile_picture')
        exclude = ['user']


class EditIdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        exclude = ['creator']
