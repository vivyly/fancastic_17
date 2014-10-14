from django.contrib import admin
from django.db import models
from django.utils import timezone

from users.models import User
from common.models import AutoDateTimeField

class FanUserAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('username','created')}

class FanUser(User):

    """ Inherited from User class
        Required:
        Username (30 char or fewer)
        password
        email
        ------------------------
        Other fields that are available are optional.
        first_name (max 30 char)
        last_name (max 30 char)
        is_staff (bool, default=False)
        is_active (bool, default=True)
        date_joined
        ------------------------
        manager is UserManager()
    """
    created        = models.DateTimeField(default=timezone.now)
    updated        = AutoDateTimeField(default=timezone.now)
    slug           = models.SlugField(max_length=50, null=False)
    is_contributor = models.BooleanField(default=False)
    desc           = models.TextField(blank=True)
