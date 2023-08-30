from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie

def home(request):
   ## return HttpResponse('<h1>Welcome to home page</h1>')
   ##return render(request, 'home.html', {'name':'Ana Rodriguez'})
   ###movies = Movie.objects.all()
   ###return render(request, 'home.html', {'movies': movies})
   searchTerm = request.GET.get('searchMovie')
   if searchTerm:
       movies = Movie.objects.filter(title__icontains=searchTerm)
   else: 
       movies = Movie.objects.all()
   return render(request, 'home.html', {'searchTerm': searchTerm, 'movies': movies})    

def about(request):
    return render(request, 'about.html')

# Create your views here.
