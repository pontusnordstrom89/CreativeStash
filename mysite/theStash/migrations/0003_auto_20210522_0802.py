# Generated by Django 3.0.13 on 2021-05-22 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theStash', '0002_profile_user_interests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='user_interests',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='./media/profilepics/'),
        ),
    ]
