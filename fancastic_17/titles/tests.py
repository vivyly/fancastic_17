import nose.tools as nt
import factory
from django.test import TestCase
from titles.models import Title


class TitleFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Title
    title_name = "Cowboy Bebop"
    plot = "The futuristic misadventures and tragedies of an easygoing bounty hunter and his partners."
    title_type = Title.TITLE_TYPES[0]
    status = Title.STATUS_CHOICE[1]

class TestTitleCreation(TestCase):

    def setUp(self):
        self.title1 = TitleFactory.create(released_year=None)

    def tearDown(self):
        self.title1.delete()

    def test_title_created(self):
        nt.eq_(self.title1.title_name, "Cowboy Bebop")
        nt.eq_(self.title1.released_year, None)
        nt.eq_(self.title1.plot,
               "The futuristic misadventures and tragedies of an easygoing bounty hunter and his partners.")
        nt.eq_(self.title1.title_type, "movie")
        nt.eq_(self.title1.status, "pre-production")

