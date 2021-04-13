from django import forms


from theStash.models import Idea, Category


class CreateIdeaForm(forms.ModelForm):

    class Meta:
        model = Idea
        fields = ['idea_title', 'idea_description',
                  'idea_category', 'is_public']


class CreateCategoryFrom(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'

