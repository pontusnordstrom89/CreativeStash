# Generated by Django 3.0.13 on 2021-05-22 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theStash', '0003_auto_20210522_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='./media/'),
        ),
    ]
