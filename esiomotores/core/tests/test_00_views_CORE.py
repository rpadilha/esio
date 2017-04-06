from django.shortcuts import resolve_url as r
from django.test import TestCase
from unittest import skip
from esiomotores.core.forms import CustomerMKTForm
from esiomotores.core.models import CustomerMKT


class ViewHomeGet(TestCase):
    def setUp(self):
        data = CustomerMKTForm()
        self.response = self.client.get(r('home'))

    def test_home(self):
        """Get HOME url should return 200 OK"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """index.html should be render with HOME url"""
        self.assertTemplateUsed(self.response, 'index.html')

    def test_html(self):
        """index.html should contains some tags"""
        contents = (('<input', 3),
                    ('name="name"',1),
                    ('name="email"',1),
                    ('type="submit"',1))

        for text, count in contents:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_blog_preview(self):
        """blog_preview should be passed in context"""
        main = self.response.context['blog_preview']
        self.assertIsInstance(main, list)

    def test_csrf(self):
        """HTML must contains CSRF"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')


class ViewAboutGet(TestCase):
    def setUp(self):
        self.response = self.client.get(r('about'))

    def test_home(self):
        """Get HOME url should return 200 OK"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """about.html should be render with ABOUT url"""
        self.assertTemplateUsed(self.response, 'about.html')

    def test_template_extends(self):
        """template should extends base.html"""
        self.assertTemplateUsed(self.response, 'base.html')

    def test_html(self):
        """index.html should contains some tags"""
        contents = (('<input', 3),
                    ('name="name"',1),
                    ('name="email"',1),
                    ('type="submit"',1))

        for text, count in contents:
            with self.subTest():
                self.assertContains(self.response, text, count)

class ViewSolutionstGet(TestCase):
    def setUp(self):
        self.response = self.client.get(r('solutions'))

    def test_home(self):
        """Get HOME url should return 200 OK"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """about.html should be render with ABOUT url"""
        self.assertTemplateUsed(self.response, 'solutions.html')

    def test_template_extends(self):
        """template should extends base.html"""
        self.assertTemplateUsed(self.response, 'base.html')

    def test_html(self):
        """index.html should contains some tags"""
        contents = (('<input', 3),
                    ('name="name"',1),
                    ('name="email"',1),
                    ('type="submit"',1))

        for text, count in contents:
            with self.subTest():
                self.assertContains(self.response, text, count)

class CustomerMKTPost(TestCase):
    fixtures = ['blog.json', 'content.json']

    def setUp(self):
        self.data = dict(name='Renato Padilha', email='tonare@gmail.com')

    def test_post(self):
        """Valid POST should redirect to HOME"""
        self.response = self.client.post(r('home'), self.data)
        self.assertEqual(302, self.response.status_code)

    def test_save_contact(self):
        self.response = self.client.post(r('home'), self.data)
        self.assertTrue(CustomerMKT.objects.exists())

    def test_home_redirect(self):
        """Valid POST origined at HOME should redirect to HOME"""
        self.response = self.client.post(r('home'), self.data)
        self.assertRedirects(self.response, '/#cadastro')

    def test_about_redirect(self):
        """Valid POST origined at ABOUT should redirect to ABOUT"""
        self.response = self.client.post(r('about'), self.data)
        self.assertRedirects(self.response, '/institucional/#cadastro')

    def test_solutions_redirect(self):
        """Valid POST origined at SOLUTIONS should redirect to SOLUTIONS"""
        self.response = self.client.post(r('solutions'), self.data)
        self.assertRedirects(self.response, '/solucoes/#cadastro')

    def test_blog_redirect(self):
        """Valid POST origined at BLOG should redirect to BLOG"""
        self.response = self.client.post(r('blog', category='geral', page=1), self.data)
        self.assertRedirects(self.response, '/noticias/geral/1/#cadastro')
