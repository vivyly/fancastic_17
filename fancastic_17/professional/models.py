from django.contrib import admin
from django.db import models
from django.utils import timezone

from common.models import AutoDateTimeField
#from pictures.models import Picture

class ProfessionalAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('fullname','created')}


class Professional(models.Model):
    slug        = models.SlugField(max_length=50, null=False)
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

