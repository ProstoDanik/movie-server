from django.urls import path
from watch.views import brother, venom, brbad, stay, flash, psycho, venomvideo, stayvideo, brbadvideo, bratvideo, flashvideo, psychovideo, fightclub, fightclubvideo, social, socialvideo, avengers, avengersvideo, war, warvideo, farfromhome, farfromhomevideo, boys, boysvideo, doctor, doctorvideo, all, allvideo, bullet, bulletvideo, island, islandvideo, mem, memvideo, lars, larsvideo, oppen, oppenvideo, pacan, pacanvideo

app_name = 'watch'

urlpatterns = [
    path('1', venom, name='Venom'),
    path('2', stay, name='Stay'),
    path('3', brbad, name='BrBad'),
    path('4', brother, name='Brat2'),
    path('5', flash, name='Flash'),
    path('6', psycho, name='Psycho'),
    path('7', social, name='Social'),
    path('8', avengers, name='Avengers'),
    path('9', war, name='War'),
    path('10', farfromhome, name='FarFromHome'),
    path('11', fightclub, name='Fight'),
    path('12', boys, name='Boys'),
    path('13', doctor, name='Doctor'),
    path('14', all, name='All'),
    path('15', bullet, name='Bullet'),
    path('16', island, name='Island'),
    path('17', mem, name='Mem'),
    path('18', lars, name='Lars'),
    path('19', oppen, name='Oppen'),
    path('20', pacan, name='Pacan'),

    path('1/watch', venomvideo, name='VenomVideo'),
    path('2/watch', stayvideo, name='StayVideo'),
    path('3/watch', brbadvideo, name='BrBadVideo'),
    path('4/watch', bratvideo, name='Brat2Video'),
    path('5/watch', flashvideo, name='FlashVideo'),
    path('6/watch', psychovideo, name='PsychoVideo'),
    path('7/watch', socialvideo, name='SocialVideo'),
    path('8/watch', avengersvideo, name='AvengersVideo'),
    path('9/watch', warvideo, name='WarVideo'),
    path('10/watch', farfromhomevideo, name='FarFromHomeVideo'),
    path('11/watch', fightclubvideo, name='FightVideo'),
    path('12/watch', boysvideo, name='BoysVideo'),
    path('13/watch', doctorvideo, name='DoctorVideo'),
    path('14/watch', allvideo, name='AllVideo'),
    path('15/watch', bulletvideo, name='BulletVideo'),
    path('16/watch', islandvideo, name='IslandVideo'),
    path('17/watch', memvideo, name='MemVideo'),
    path('18/watch', larsvideo, name='LarsVideo'),
    path('19/watch', oppenvideo, name='OppenVideo'),
    path('20/watch', pacanvideo, name='PacanVideo'),
]