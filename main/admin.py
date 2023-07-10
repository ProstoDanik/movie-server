from django.contrib import admin
from main.models import Genre, FilmDescription, Favorites

# Register your models here.
admin.site.register(Genre)
admin.site.register(FilmDescription)
admin.site.register(Favorites)
