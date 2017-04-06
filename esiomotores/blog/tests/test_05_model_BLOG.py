from django.core.exceptions import ValidationError
from django.test import TestCase
from django.shortcuts import resolve_url as r
from esiomotores.blog.models import Blogs


class BlogMainModelTest(TestCase):
    def setUp(self):
        self.blog = Blogs.objects.create(title='Promoção Gamma Ferramentas - Março/17',
                                         slug='promocao-gamma-ferramentas-marco17', category=Blogs.PROMO)

    def test_create(self):
        self.assertTrue(Blogs.objects.exists())

    def test_catalog(self):
        blog = Blogs.objects.create(title='Catalogo', slug='catalogo', category=Blogs.CATALOG)
        self.assertTrue(Blogs.objects.exists())

    def test_event(self):
        blog = Blogs.objects.create(title='Evento', slug='evento', category=Blogs.EVENT)
        self.assertTrue(Blogs.objects.exists())

    def test_news(self):
        blog = Blogs.objects.create(title='Noticia', slug='noticia', category=Blogs.NEWS)
        self.assertTrue(Blogs.objects.exists())

    def test_promo(self):
        blog = Blogs.objects.create(title='Promoção', slug='promocao', category=Blogs.PROMO)
        self.assertTrue(Blogs.objects.exists())

    def test_other(self):
        blog = Blogs.objects.create(title='Outro', slug='outro', category=Blogs.OTHER)
        self.assertTrue(Blogs.objects.exists())

    def test_choices(self):
        '''Category should be limited to Catalogos, Eventos, Novidades, Promocoes, Outros'''
        blog = Blogs.objects.create(
            title='Promoção Fake',
            slug='promocao-fake',
            category='Z')

        self.assertRaises(ValidationError, blog.full_clean)

    def test_slug_cant_be_blank(self):
        field = Blogs._meta.get_field('slug')
        self.assertFalse(field.blank)

    def test_str(self):
        self.assertEqual('Promoção Gamma Ferramentas - Março/17', str(self.blog))

    def test_get_absolute_url(self):
       url = r('one_blog', slug=self.blog.slug)
       self.assertEqual(url, self.blog.get_absolute_url())