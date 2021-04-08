from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    #profession = models.CharField(max_length=30)
    twitter = models.CharField(max_length=30)
    instagram = models.CharField(max_length=30)
    vimeo = models.CharField(max_length=30)
    behance = models.CharField(max_length=30)
    github = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.user}:{self.bio}"


class Idea(models.Model):
    title = models.CharField(max_length=30)
    #image = models.ImageField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="creator")
    description = models.TextField(blank=True)
    #an idea can be turned public but is private by default
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Category(models.Model):
    c_name = models.CharField(max_length=30, primary_key=True)
    idea = models.ManyToManyField(Idea, through='Interest', through_fields=('c_name', 'idea'),
    )

    def __str__(self):
        return self.name

class Interest(models.Model):
    c_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
