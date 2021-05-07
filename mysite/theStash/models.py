from django.contrib.auth.models import User
from django.db import models
from datetime import date


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100, primary_key=True)
    user_interests = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.category_name

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_profile")
    bio = models.TextField(blank=True)
    #profile_picture = models.Image()
    #social links connected to user profile
    link1 = models.URLField(max_length=200, blank=True)
    link2 = models.URLField(max_length=200, blank=True)
    link3 = models.URLField(max_length=200, blank=True)
    #user_interests = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.bio



class Idea(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    idea_title = models.CharField(max_length=30)
    idea_description = models.TextField(blank=True)
    #an idea can be turned public but is private by default
    idea_category = models.ManyToManyField(Category, related_name="list_idea_categories")
    is_public = models.BooleanField(default=False)
    image = models.ImageField(upload_to='./media/', null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    updated_when = models.DateField(auto_now=True)


    def __str__(self):
        return self.idea_title
