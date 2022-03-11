from pyexpat import model
from statistics import mode
from unicodedata import category, name
from django.db import models
from django.urls import reverse

# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    active = models.BooleanField()
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'bands/{self.slug}'


class News(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField();
    author = models.CharField(max_length=200, null=True)
    text = models.TextField(null=True)
    slug = models.SlugField(max_length=255, unique=True)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)+' '+self.title

    def get_absolute_url(self):
        return f'news/{self.slug}'
        


class MusicAlbum(models.Model):
    name = models.CharField(max_length=255)
    create = models.DateField()
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255)
    
    def __str__(self):
        return self.name

class Tracks(models.Model):

    band = models.ForeignKey(Band, on_delete=models.CASCADE, null=True)
    MusicAlbum = models.ForeignKey(MusicAlbum, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    text = models.TextField()
    
    def __str__(self):
        return self.name

    
