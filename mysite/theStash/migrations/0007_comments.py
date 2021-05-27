# Generated by Django 3.0.13 on 2021-05-25 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theStash', '0006_auto_20210524_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idea_comment', models.TextField()),
                ('comment_likes', models.IntegerField(blank=True)),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theStash.Idea')),
            ],
        ),
    ]