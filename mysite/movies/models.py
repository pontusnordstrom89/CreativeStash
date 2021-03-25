from django.db import models

class Genre(models.Model):
    genre_name = models.CharField(primary_key=True, max_length=100)
    genre_decription = models.TextField(max_length=1000)

    def __str__(self):
        self.genre = self.genre_name + ' | ' + self.genre_decription
        return self.genre


class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    movie_titel = models.CharField(max_length=100)
    movie_description = models.TextField(max_length=1000)
    release_date = models.DateField('Release date')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        self.movie = str(self.movie_id) + ' | ' + self.movie_titel
        return self.movie
