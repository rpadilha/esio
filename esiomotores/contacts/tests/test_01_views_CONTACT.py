from django.core import mail
from django.shortcuts import resolve_url as r
from django.test import TestCase
from esiomotores.contacts.forms import ContactForm
from esiomotores.contacts.models import Contact


class ViewContactGet(TestCase):
    def setUp(self):
        self.response = self.client.get(r('contacts'))

    def test_home(self):
        """Get HOME url should return 200 OK"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """about.html should be render with ABOUT url"""
        self.assertTemplateUsed(self.response, 'contact.html')

    def test_template_includes_nav(self):
        """template should include nav.html"""
        self.assertTemplateUsed(self.response, 'nav.html')

    def test_template_includes_footer(self):
        """template should include footer.html"""
        self.assertTemplateUsed(self.response, 'footer_simple.html')

    def test_html(self):
        """"HTML must contain input tags"""
        tags = (('<form',1),
                ('<input', 4),
                ('<textarea',1),
                ('<label', 4),
                ('type="text"', 2),
                ('type="submit"',1),
                ('type="reset"',1))

        for text,count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_csrf(self):
        """"HTML must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """"Context must have contact form"""
        form = self.response.context['form']
        self.assertIsInstance(form, ContactForm)


class ContactMessagePostValid(TestCase):
    def setUp(self):
        data = dict(name='Renato Padilha', email='tonare@gmail.com', phone='21988010276',
                    msg='Como faço para realizar pedidos fora do horário comercial?', ipaddr='127.0.0.1')
        self.response = self.client.post('/contato/', data)

    def test_post(self):
        """Valid POST should redirect to /contato/"""
        self.assertEqual(302, self.response.status_code)

    def test_send_contact_email(self):
        """1 email should be sent"""
        self.assertEqual(1, len(mail.outbox))

    def test_save_contact(self):
        self.assertTrue(Contact.objects.exists())


class ContactMessagePostInvalid(TestCase):
    def setUp(self):
        self.response = self.client.post('/contato/', {})

    def test_post(self):
        """Invalid POST should not redirect"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'contact.html')

    def test_has_form(self):
        """"When we got an error in the form, form should be sent in the context"""
        form = self.response.context['form']
        self.assertIsInstance(form, ContactForm)

    def test_form_has_errors(self):
        """"Errors should be returned through render return"""
        form = self.response.context['form']
        self.assertTrue(form._errors)

    def test_not_save_subscription(self):
        self.assertFalse(Contact.objects.exists())


class ContactMessageSuccess(TestCase):
    def setUp(self):
        self.data = dict(name='Renato Padilha', email='tonare@gmail.com', phone='21988010276',
                    msg='Como faço para realizar pedidos fora do horário comercial?', ipaddr='127.0.0.1')

    def test_message(self):
        response = self.client.post('/contato/', self.data, follow=True)
        self.assertContains(response, 'Mensagem enviada com sucesso!')

