from django.db import models

from users.models import User

class Genre(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class FilmDescription(models.Model):
    name = models.CharField(max_length=128)
    genres = models.CharField(max_length=128)
    time = models.CharField(max_length=50)
    image = models.ImageField(upload_to='films_images')
    link = models.CharField(max_length=128, default='')
    category = models.ForeignKey(to=Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f'Фильм: {self.name} | Жанр: {self.genres}'


class Favorites(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    film = models.ForeignKey(to=FilmDescription, on_delete=models.CASCADE)

    def __str__(self):
        return f'Избранные для: {self.user.username} | Фильм: {self.film.name}'


class Rating(models.Model):
    rating = models.CharField(max_length=2)

    def __str__(self):
        return self.rating


class Reviews(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    film = models.ForeignKey(to=FilmDescription, on_delete=models.CASCADE)
    rating_number = models.ForeignKey(to=Rating, on_delete=models.CASCADE)
    text_reviews = models.TextField(max_length=2000)

    def __str__(self):
        return f'Отзыв от: {self.user.username} | Фильм: {self.film.name}'