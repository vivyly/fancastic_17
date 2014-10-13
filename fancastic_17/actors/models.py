from django.db import models
from django.utils import timezone

from common.models import AutoDateTimeField
from titles.models import Title
#from pictures.models import Picture

class Actor(models.Model):
    #slug        = models.SlugField(unique=True)
    fullname    = models.CharField(max_length=100, blank=True)
    created     = models.DateTimeField(default=timezone.now)
    updated     = AutoDateTimeField(default=timezone.now)
    height      = models.CharField(max_length=10, blank=True)
    is_alive    = models.BooleanField(default=True)
    is_active   = models.BooleanField(default=True)
    birthday    = models.IntegerField(blank=True, null=True)
    birthmonth  = models.IntegerField(blank=True, null=True)
    birthyear   = models.IntegerField(blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True)
    url         = models.URLField(blank=True)
    imdb        = models.URLField(blank=True)
    #picture    = models.ForeignKey(Picture, null=True))


class Role(models.Model):
    actor       = models.ForeignKey(Actor)
    media_title = models.ForeignKey(Title)
    ROLE_CHOICES = [
        'Director',
        'Writer',
        'Producer',
        'Music',
        'Cinematography',
        'Crew',
        'Actor',
    ]
    role        = models.CharField(max_length=20, 
                  choices=((x,x) for x in ROLE_CHOICES),
                  default = 'Actor')

    character   = models.CharField(max_length=100)
    desc        = models.TextField(blank=True)
    url         = models.URLField(blank=True)
    imdb        = models.URLField(blank=True)
    #picture     = models.ForeignKey(Picture, null=True)


