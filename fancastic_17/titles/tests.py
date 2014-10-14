import nose.tools as nt
import factory
from django.test import TestCase
from titles.models import SourceMaterial, Adaptation


class SourceMaterialFactory(factory.DjangoModelFactory):
    FACTORY_FOR = SourceMaterial
    source_name = "Cowboy Bebop"
    plot = "The futuristic misadventures and tragedies of an easygoing bounty hunter and his partners."
    slug = '123test'
    source_creator = 'Cain Kuga'
    released_year  = 1997
    source_type   = 'anime'

class SourceMaterialCreation(TestCase):

    def setUp(self):
        self.title1 = SourceMaterialFactory.create()

    def tearDown(self):
        self.title1.delete()

    def test_title_created(self):
        nt.eq_(self.title1.source_name, "Cowboy Bebop")
        nt.eq_(self.title1.released_year, 1997)
        nt.eq_(self.title1.plot,
               "The futuristic misadventures and tragedies of an easygoing bounty hunter and his partners.")
        nt.eq_(self.title1.source_type, "anime")
        nt.eq_(self.title1.source_creator, 'Cain Kuga')
        nt.eq_(self.title1.slug, "123test")


class AdaptationFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Adaptation
    adaptation_name = "Space Cowboy"
    plot            = "The futuristic misadventures and tragedies of an easygoing bounty hunter and his partners."
    slug            = '123test'
    source_material = factory.SubFactory(SourceMaterialFactory)
    release_year    = 2018
    rights_owner    = '20th Century Fox'
    adapt_media     = Adaptation.ADAPT_MEDIA[0]
    adapt_type      = Adaptation.ADAPT_TYPE[6]
    status          = Adaptation.STATUS_CHOICE[1]

class TestAdaptationCreation(TestCase):

    def setUp(self):
        self.title1 = AdaptationFactory.create()

    def tearDown(self):
        self.title1.delete()

    def test_title_created(self):
        nt.eq_(self.title1.adaptation_name, "Space Cowboy")
        nt.eq_(self.title1.release_year, 2018)
        nt.eq_(self.title1.plot,
               "The futuristic misadventures and tragedies of an easygoing bounty hunter and his partners.")
        nt.eq_(self.title1.slug, '123test')
        nt.eq_(self.title1.rights_owner, '20th Century Fox')
        nt.eq_(self.title1.adapt_media, "movie")
        nt.eq_(self.title1.adapt_type, "inspired")
        nt.eq_(self.title1.status, "announced")
