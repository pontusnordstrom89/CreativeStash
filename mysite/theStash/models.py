from django.db import models

# Create your models here.

class Profil(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.TextField(blank=True)
    #join_date = models.DateField()
    #profession = models.CharField(max_length=30)
    twitter = models.TextField(blank=True)
    instagram = models.TextField(blank=True)
    vimeo = models.TextField(blank=True)
    behance = models.TextField(blank=True)
    github = models.TextField(blank=True)


class Idea(models.Model):
    title = models.CharField(max_length=30)
    #image = models.ImageField()
    description = models.TextField(blank=True)


class Category(models.Model):
    c_name = models.CharField(max_length=30)
