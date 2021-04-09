from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    #profession = models.CharField(max_length=30)
    twitter = models.CharField(max_length=100, blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    vimeo = models.CharField(max_length=100, blank=True)
    behance = models.CharField(max_length=100, blank=True)
    github = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user}:{self.bio}"


class Category(models.Model):
    category_name = models.CharField(max_length=30, primary_key=True)
    category_description = models.TextField(max_length=500)

    def __str__(self):
        return self.category_name

class Idea(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    idea_title = models.CharField(max_length=30)
    #image = models.ImageField()
    idea_description = models.TextField(blank=True)
    #an idea can be turned public but is private by default
    is_public = models.BooleanField(default=False)
    idea_category = models.ManyToManyField(Category)

    def __str__(self):
        return self.idea_title


class Interest(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
