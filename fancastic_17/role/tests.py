import nose.tools as nt
import factory
from django.test import TestCase

from professional.models import Professional
from character.models import Character
from titles.models import Adaptation

from role.models import Role

class RoleFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Role

class TestRoleCreation(TestCase):
    pass
