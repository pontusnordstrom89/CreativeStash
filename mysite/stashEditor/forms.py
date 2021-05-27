from django import forms
from theStash.models import Idea, Category


class CreateIdeaForm(forms.ModelForm):

    class Meta:
        model = Idea
        fields = ['idea_title', 'idea_description', 'is_public', 'image']


class CreateCategoryFrom(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['category_name']


