from django import forms
from theStash.models import Profile

class EditSocialProfile(forms.ModelForm):
    class Meta:
        model= Profile
        fields= ['bio','link1','link2','link3']




