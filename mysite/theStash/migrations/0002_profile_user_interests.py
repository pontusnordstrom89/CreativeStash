# Generated by Django 3.0.13 on 2021-05-20 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theStash', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_interests',
            field=models.ManyToManyField(blank=True, to='theStash.Category'),
        ),
    ]