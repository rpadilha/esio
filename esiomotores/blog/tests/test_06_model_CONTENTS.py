from django.test import TestCase
from esiomotores.blog.models import Blogs, Contents


class ContentsGet(TestCase):
    def setUp(self):
        self.title = Blogs.objects.create(
            title = 'Nova Notícia',
            publish = True,
            slug = 'nova-noticia'
        )

    def test_create(self):
        content = Contents.objects.create(
            title = self.title,
            order_out = 1,
            text = 'Você não pode perder a mais nova promoção da Gamma!',
            picture = 'blogpicture.png',
            inverse = False
        )
        self.assertTrue(Contents.objects.exists())

    def test_order_out_cant_be_blank(self):
        field = Contents._meta.get_field('order_out')
        self.assertFalse(field.blank)

    def test_str(self):
        content = Contents(
            title=self.title,
            order_out=1,
            text='Você não pode perder a mais nova promoção da Gamma!',
            picture='blogpicture.png',
            inverse=False
        )
        self.assertEqual('1', str(content))
