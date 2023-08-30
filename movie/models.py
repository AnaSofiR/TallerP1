from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100, default=' ')
    description = models.CharField(max_length=250, default=' ')
    image = models.ImageField(upload_to='movie/images/', default=' ')
    url = models.URLField(blank=True, default=' ')