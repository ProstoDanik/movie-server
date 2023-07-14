from django.contrib import admin
from main.models import Genre, FilmDescription, Favorites, Rating, Reviews

# Register your models here.
admin.site.register(Genre)
admin.site.register(FilmDescription)
admin.site.register(Favorites)
admin.site.register(Rating)
admin.site.register(Reviews)
