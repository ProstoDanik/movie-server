from django.shortcuts import render
from watch.models import DetailFilm

# Create your views here.
def brother(request):
    context = {
        'films': DetailFilm.objects.get(id=4),
    }
    return render(request, 'watch/Brat2.html', context)


def venom(request):
    context = {
        'films': DetailFilm.objects.get(id=1),
    }
    return render(request, 'watch/Venom.html', context)


def brbad(request):
    context = {
        'films': DetailFilm.objects.get(id=3),
    }
    return render(request, 'watch/BrBad.html', context)


def stay(request):
    context = {
        'films': DetailFilm.objects.get(id=2),
    }
    return render(request, 'watch/Stay.html', context)


def flash(request):
    context = {
        'films': DetailFilm.objects.get(id=5),
    }
    return render(request, 'watch/Flash.html', context)


def psycho(request):
    context = {
        'films': DetailFilm.objects.get(id=6),
    }
    return render(request, 'watch/Psycho.html', context)


def venomvideo(request):
    return render(request, 'watch/VenomVideo.html')


def stayvideo(request):
    return render(request, 'watch/StayVideo.html')


def brbadvideo(request):
    return render(request, 'watch/BrBadVideo.html')


def bratvideo(request):
    return render(request, 'watch/Brat2Video.html')


def flashvideo(request):
    return render(request, 'watch/FlashVideo.html')


def psychovideo(request):
    return render(request, 'watch/PsychoVideo.html')


def fightclub(request):
    context = {
        'films': DetailFilm.objects.get(id=11),
    }
    return render(request, 'watch/FightClub.html', context)


def fightclubvideo(request):
    return render(request, 'watch/FightClubVideo.html')


def social(request):
    context = {
        'films': DetailFilm.objects.get(id=7),
    }
    return render(request, 'watch/Social.html', context)


def socialvideo(request):
    return render(request, 'watch/SocialVideo.html')


def avengers(request):
    context = {
        'films': DetailFilm.objects.get(id=8),
    }
    return render(request, 'watch/Avengers.html', context)


def avengersvideo(request):
    return render(request, 'watch/AvengersVideo.html')


def war(request):
    context = {
        'films': DetailFilm.objects.get(id=9),
    }
    return render(request, 'watch/War.html', context)


def warvideo(request):
    return render(request, 'watch/WarVideo.html')


def farfromhome(request):
    context = {
        'films': DetailFilm.objects.get(id=10),
    }
    return render(request, 'watch/FarFromHome.html', context)


def farfromhomevideo(request):
    return render(request, 'watch/FarFromHomeVideo.html')


def boys(request):
    context = {
        'films': DetailFilm.objects.get(id=12),
    }
    return render(request, 'watch/Boys.html', context)


def boysvideo(request):
    return render(request, 'watch/BoysVideo.html')