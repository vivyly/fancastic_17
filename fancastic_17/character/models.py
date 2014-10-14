from django.db import models
from titles.models import Adaptation

class Character(models.Model):
    character_name   = models.CharField(max_length=100)
    title            = models.ForeignKey(Adaptation)
    STATUS_CHOICE = [
        "original",
        "unknown",
        "rumored",
        "source",
    ]
    character_status = models.CharField(max_length=10,
                                        choices = ((x, x) for x in STATUS_CHOICE),
                                        default = 'source')
