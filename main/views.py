from django.shortcuts import render, HttpResponseRedirect, reverse
from main.models import Genre, FilmDescription, Favorites, Rating
from users.models import User
from django.contrib.auth.decorators import login_required
from main.forms import ReviewForm


# Create your views here.

def welcome(request):
    return render(request, 'main/welcome.html')


def index(request, genre_id=None):
    search_query = request.GET.get('search', '')

    if search_query == None:
        films = FilmDescription.objects.all()
    elif genre_id:
        genre = Genre.objects.get(id=genre_id)
        films = FilmDescription.objects.filter(category=genre)
    else:
        films = FilmDescription.objects.filter(name__iregex=search_query)

    context = {
        'films': films,
        'genres': Genre.objects.all(),
    }
    return render(request, 'main/index.html', context)



def review(request):
    context = {
        'films': FilmDescription.objects.all(),
        'ratings': Rating.objects.all(),


    }
    return render(request, 'main/reviews.html', context)



@login_required
def favorites_add(request, film_id):
    film = FilmDescription.objects.get(id=film_id)
    favorites = Favorites.objects.filter(user=request.user, film=film)

    if not favorites.exists():
        Favorites.objects.create(user=request.user, film=film)
    else:
        favorite = favorites.first()
        favorite.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def favorite_remove(request, favorite_id):
    favorite = Favorites.objects.get(id=favorite_id)
    favorite.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])