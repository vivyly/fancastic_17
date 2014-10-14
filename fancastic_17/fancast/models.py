from django.db import models
from django.utils import timezone

from common.models import AutoDateTimeField
from professional.models import Professional
from role.models import Role
from fan.models import FanUser

class FanCast(models.Model):
    creator      = models.ForeignKey(FanUser)
    created      = models.DateTimeField(default=timezone.now)
    updated      = AutoDateTimeField(default=timezone.now)
    professional = models.ForeignKey(Professional)
    role         = models.ForeignKey(Role)
    CASTING_STATUS = [
        'unknown',
        'rumored',
        'negotiation',
        'confirmed',
        'rejected',
        'replaced',
    ]
    status       = models.CharField(max_length=10,
                                    choices=((x,x) for x in CASTING_STATUS),
                                    default='unknown')
