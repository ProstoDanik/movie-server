"""movie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from main.views import welcome, index, review, favorites_add, favorite_remove

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', welcome, name='welcome'),
    path('catalog/', index, name='index'),
    path('catalog/genre/<int:genre_id>/', index, name='genre'),
    path('catalog/reviews/', review, name='review'),

    path('favorites/add/<int:film_id>/', favorites_add, name='favorites_add'),
    path('favorites/remove/<int:favorite_id>/', favorite_remove, name='favorite_remove'),


    path('films/', include('watch.urls', namespace='watch')),
    path('users/', include('users.urls', namespace='users')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)