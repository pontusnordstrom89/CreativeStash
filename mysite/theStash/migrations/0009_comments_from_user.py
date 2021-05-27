# Generated by Django 3.0.13 on 2021-05-27 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('theStash', '0008_auto_20210526_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='from_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
