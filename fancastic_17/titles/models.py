from django.db import models

class Title(models.Model):
    title_name    = models.CharField(max_length=100)
    released_year = models.IntegerField(blank=True, null=True)
    plot          = models.TextField()
    TITLE_TYPES = [
        'movie',
        'tvshow',
        'miniseries',
        'musical',
        'animation',
        'short',
    ]
    title_type    = models.CharField(max_length=10,
                                     choices = ((x,x) for x in TITLE_TYPES),
                                     default = 'movie')
    STATUS_CHOICE = [
        'announced',
        'pre-production',
        'filming',
        'post-production',
        'released'
    ]
    status        = models.CharField(max_length=20,
                                     choices = ((x,x) for x in STATUS_CHOICE),
                                     default = 'announced')

