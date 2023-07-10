from django.db import models

# Create your models here.
class DetailFilm(models.Model):
    name = models.CharField(max_length=128)
    eng_name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='detail_images')
    description = models.CharField(max_length=1000)
    year = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    genre = models.CharField(max_length=128)
    slogan = models.CharField(max_length=200)
    director = models.CharField(max_length=128)
    time = models.CharField(max_length=128)
    rating = models.CharField(max_length=128)
    num_rating = models.CharField(max_length=128)
    reviews = models.CharField(max_length=128)

    def __str__(self):
        return f'Фильм: {self.name}'