# Generated by Django 3.0.13 on 2021-04-17 08:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True)),
                ('twitter', models.CharField(blank=True, max_length=100)),
                ('instagram', models.CharField(blank=True, max_length=100)),
                ('vimeo', models.CharField(blank=True, max_length=100)),
                ('behance', models.CharField(blank=True, max_length=100)),
                ('github', models.CharField(blank=True, max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_interests', models.ManyToManyField(to='theStash.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idea_title', models.CharField(max_length=30)),
                ('idea_description', models.TextField(blank=True)),
                ('is_public', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL)),
                ('idea_category', models.ManyToManyField(to='theStash.Category')),
            ],
        ),
    ]