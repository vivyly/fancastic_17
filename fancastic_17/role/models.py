from django.db import models

from professional.models import Professional
from titles.models import Adaptation
from character.models import Character

class Role(models.Model):
    title  = models.ForeignKey(Adaptation)
    character    = models.ForeignKey(Character, null=True)
    ROLE_CHOICES = [
        'Director',
        'Writer',
        'Producer',
        'Music',
        'Cinematography',
        'Crew',
        'Actor',
    ]
    role         = models.CharField(max_length=20, 
                  choices=((x,x) for x in ROLE_CHOICES),
                  default = 'Actor')
    desc         = models.TextField(blank=True)
    url          = models.URLField(blank=True)
    imdb         = models.URLField(blank=True)
    #picture     = models.ForeignKey(Picture, null=True)

