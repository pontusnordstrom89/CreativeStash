from django import forms
from theStash.models import theStash_profile

class EditSocialProfile(forms.ModelForm):
    class Meta:
        model= Profile
        fields= ['bio','link1','link2','link3']


