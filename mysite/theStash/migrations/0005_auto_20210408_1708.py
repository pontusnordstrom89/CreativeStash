# Generated by Django 3.0.13 on 2021-04-08 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theStash', '0004_auto_20210403_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='behance',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='github',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='instagram',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='vimeo',
            field=models.CharField(max_length=30),
        ),
    ]
