from django.urls import path, re_path
from django.conf.urls import url
from . import views


app_name = 'stashProfile'
urlpatterns = [
    path('profile_settings', views.profile_settings, name='profile_settings'),
    path('social_profile/<int:user_profile_id>', views.social_profile, name='social_profile'),
    path('edit_social_profile/<int:user_profile_id>', views.edit_social_profile, name='edit_social_profile'),
    path('edit_idea/<int:idea_id>', views.edit_idea, name='edit_idea'),
    ]
