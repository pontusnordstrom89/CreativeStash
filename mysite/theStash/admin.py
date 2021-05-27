from django.contrib import admin

from .models import Profile, Idea, Category, Comments

admin.site.register(Profile)
admin.site.register(Idea)
admin.site.register(Category)
admin.site.register(Comments)

