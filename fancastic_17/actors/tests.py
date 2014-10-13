import nose.tools as nt
import factory
from django.test import TestCase
from actors.models import Actor


class ActorFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Actor
    fullname = "Maisie Williams"
    height = "5'0\""
    is_alive = True
    is_active = True
    birthday = 15
    birthmonth = 4
    birthyear = 1997
    nationality = "British"
    url = "http://en.wikipedia.org/wiki/Maisie_Williams"
    imdb = "http://www.imdb.com/name/nm3586035/"


class TestActorCreation(TestCase):

    def setUp(self):
        self.actor1 = ActorFactory.create()

    def tearDown(self):
        self.actor1.delete()

    def test_actor_created(self):
        nt.eq_(self.actor1.fullname, "Maisie Williams")
        nt.eq_(self.actor1.height, "5'0\"")
        nt.eq_(self.actor1.is_alive, True)
        nt.eq_(self.actor1.is_active, True)
        nt.eq_(self.actor1.birthday, 15)
        nt.eq_(self.actor1.birthmonth, 4)
        nt.eq_(self.actor1.birthyear, 1997)
        nt.eq_(self.actor1.nationality, "British")
        nt.eq_(self.actor1.url, "http://en.wikipedia.org/wiki/Maisie_Williams")
        nt.eq_(self.actor1.imdb, "http://www.imdb.com/name/nm3586035/")


#class RoleFactory(factory.DjangoModelFactory):
#   pass
