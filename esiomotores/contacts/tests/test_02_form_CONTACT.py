from django.test import TestCase
from esiomotores.contacts.forms import ContactForm

class ContactFormTest(TestCase):
    def test_form_has_fields(self):
        """"Form must have 5 fields """
        form = ContactForm()
        expected = ['name', 'email', 'phone', 'msg', 'ipaddr']
        self.assertSequenceEqual(list(form.fields), expected)

    def test_mobile_phone_has_11_digits(self):
        """Mobile phones must have 11 digits"""
        form = self.make_validated_form(phone='2198801027')
        self.assertFormErrorCode(form, 'phone', 'mobile_length')

    def test_fixed_phone_has_10_digits(self):
        """Fixed phones must have 11 digits"""
        form = self.make_validated_form(phone='22382440070')
        self.assertFormErrorCode(form, 'phone', 'fixed_length')

    def test_phone_is_digit(self):
        """Phones must have only digits"""
        form = self.make_validated_form(phone='ABCD')
        self.assertFormErrorCode(form, 'phone', 'digit')

    def test_name_capitalized(self):
        """Name must be capitalized"""
        form = self.make_validated_form(name='RENATO PADILHA')
        self.assertEqual('Renato Padilha', form.cleaned_data['name'])

    def test_email_lowercased(self):
        """Email must be lowercase"""
        form = self.make_validated_form(email='tonare@GMAIL.COM')
        self.assertEqual('tonare@gmail.com', form.cleaned_data['email'])

    def test_msg_lowercased (self):
        """Message must be lowercase"""
        form = self.make_validated_form(msg='GOSTARIA DE SABER O PREÇO DA TORNEIRA!!')
        self.assertEqual('gostaria de saber o preço da torneira!!', form.cleaned_data['msg'])


## As funções abaixo foram criadas para auxiliar na execução dos testes

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        error_list = errors[field]
        self.assertListEqual([msg], error_list)


    def assertFormErrorCode(self, form, field, code):
        self.assertEqual(form.errors.as_data()[field][0].code, code)


    def make_validated_form(self, **kwargs):
        VALID = dict(name='Renato Padilha', email='tonare@gmail.com', phone='21988010276',
                    msg='Teste de Mensagem', ipaddr='127.0.0.1')

        data = dict(VALID, **kwargs)
        form = ContactForm(data)
        form.is_valid()
        return form
