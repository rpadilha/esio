from django.test import TestCase
from esiomotores.core.forms import CustomerMKTForm

class CustomerMKTFormTest(TestCase):
    def test_form_has_fields(self):
        """"Form must have 5 fields """
        form = CustomerMKTForm()
        expected = ['name', 'email']
        self.assertSequenceEqual(list(form.fields), expected)

    def test_name_capitalized(self):
        """Name must be capitalized"""
        form = self.make_validated_form(name='RENATO PADILHA')
        self.assertEqual('Renato Padilha', form.cleaned_data['name'])

    def test_email_lowercased(self):
        """Email must be lowercase"""
        form = self.make_validated_form(email='tonare@GMAIL.COM')
        self.assertEqual('tonare@gmail.com', form.cleaned_data['email'])


## As funções abaixo foram criadas para auxiliar na execução dos testes

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        error_list = errors[field]
        self.assertListEqual([msg], error_list)


    def assertFormErrorCode(self, form, field, code):
        self.assertEqual(form.errors.as_data()[field][0].code, code)


    def make_validated_form(self, **kwargs):
        VALID = dict(name='Renato Padilha', email='tonare@gmail.com', phone='21988010276')

        data = dict(VALID, **kwargs)
        form = CustomerMKTForm(data)
        form.is_valid()
        return form
