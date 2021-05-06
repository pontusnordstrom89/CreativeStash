from django import forms
<<<<<<< Updated upstream
from theStash.models import Profile
=======
from theStash.models import theStash_profile
>>>>>>> Stashed changes

class EditSocialProfile(forms.ModelForm):
    class Meta:
        model= Profile
        fields= ['bio','link1','link2','link3']


<<<<<<< Updated upstream


=======
>>>>>>> Stashed changes
