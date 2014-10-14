from django.contrib import admin
from django.db import models
from django.utils import timezone

from common.models import AutoDateTimeField

class SourceMaterialAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('source_name','created')}

class SourceMaterial(models.Model):
    slug           = models.SlugField(max_length=50, null=False)
    created        = models.DateTimeField(default=timezone.now)
    updated        = AutoDateTimeField(default=timezone.now)
    source_name    = models.CharField(max_length=255)
    source_creator = models.CharField(max_length=100, blank=True)
    released_year  = models.IntegerField(blank=True, null=True)
    plot           = models.TextField(blank=True)
    SOURCE_TYPES = [
        'book',
        'comic',
        'cartoon',
        'anime',
        'movie',
        'tvshow',
        'musical',
        'parkride',
        'boardgame',
        'videogame',
        'mythology',
    ]
    source_type   = models.CharField(max_length=10,
                                    choices=((x,x) for x in SOURCE_TYPES),
                                    default='book')


class AdaptationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('adaptation_name','created')}

class Adaptation(models.Model):
    slug            = models.SlugField(max_length=50, null=False)
    created         = models.DateTimeField(default=timezone.now)
    updated         = AutoDateTimeField(default=timezone.now)
    adaptation_name = models.CharField(max_length=255)
    source_material = models.ForeignKey(SourceMaterial, null=True)
    release_year    = models.IntegerField(blank=True, null=True)
    rights_owner    = models.CharField(max_length=255)
    plot            = models.TextField(blank=True)
    ADAPT_MEDIA = [
        'movie',
        'tvshow',
        'miniseries',
        'musical',
        'animation',
        'short',
    ]
    adapt_media      = models.CharField(max_length=10,
                                     choices = ((x,x) for x in ADAPT_MEDIA),
                                     default = 'movie')
    ADAPT_TYPE = [
        'remake',
        'sequel',
        'prequel',
        'spinoff',
        'alternate',
        'original',
        'inspired',
    ]
    adapt_type      = models.CharField(max_length=20,
                                       choices = ((x,x) for x in ADAPT_TYPE),
                                       default='remake')
    STATUS_CHOICE = [
        'rumored',
        'announced',
        'pre-production',
        'filming',
        'post-production',
        'released'
    ]
    status          = models.CharField(max_length=20,
                                     choices = ((x,x) for x in STATUS_CHOICE),
                                     default = 'announced')


