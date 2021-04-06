from django import forms

from theStash.models import Idea

class CreateIdeaForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(CreateIdeaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Idea
        fields = ['title', 'profile', 'description', 'public']
