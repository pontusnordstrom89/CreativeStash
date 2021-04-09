from django import forms


from theStash.models import Idea


class CreateIdeaForm(forms.ModelForm):

    class Meta:
        model = Idea
        fields = ['idea_title', 'idea_description',
                  'idea_category', 'is_public']


