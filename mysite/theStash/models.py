from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import IntegerField


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.category_name

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_profile")
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='./profilepics/', null=True, blank=True)
    #optional social links connected to user profile
    vimeo = models.URLField(max_length=200, blank=True)
    behance = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)
    user_interests = models.ManyToManyField(Category, blank=True)

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
    
class Comments(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name="comments_idea")
    idea_comment = models.TextField()
    comment_likes = IntegerField(null= True) 
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.idea_comment

class Like(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name="likes") 
    idea_like = models.IntegerField(null=True) 


    def __str__(self):
        self.namn="test"
        return self.namn  

