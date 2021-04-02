from django.db import models

# Create your models here.

class Profile(models.Model):
    #username = models.ForeignKey(auth_user, on_delete=models.CASCADE)
    #first_name = models.ForeignKey(auth_user, on_delete=models.CASCADE)
    #last_name = models.ForeignKey(auth_user, on_delete=models.CASCADE)
    #date_joined = models.ForeignKey(auth_user, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    #profession = models.CharField(max_length=30)
    twitter = models.TextField(blank=True)
    instagram = models.TextField(blank=True)
    vimeo = models.TextField(blank=True)
    behance = models.TextField(blank=True)
    github = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Idea(models.Model):
    title = models.CharField(max_length=30)
    #image = models.ImageField()
    username = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    #an idea can be turned public but is private by default
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Category(models.Model):
    c_name = models.CharField(max_length=30, primary_key=True)
    idea = models.ManyToManyField(Idea, through='Interest')

    def __str__(self):
        return self.name

class Interest(models.Model):
    c_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
