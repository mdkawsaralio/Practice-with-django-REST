from django.shortcuts import render
from .models import Movie
from django.http import JsonResponse



# Create your views here.



def movie_list(request):
    Movies=Movie.objects.all()
    data={
        'movies':list(Movies.values())
    }
    return JsonResponse(data)


