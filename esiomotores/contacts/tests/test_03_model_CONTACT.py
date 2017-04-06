from datetime import datetime
from django.test import TestCase
from esiomotores.contacts.models import Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.obj = Contact(
            name='Renato Padilha',
            email='tonare@gmail.com',
            phone='21988010276',
            msg='Teste de mensagem',
            ipaddr='127.0.0.1'

        )
        self.obj.save()

    def test_create (self):
        self.assertTrue(Contact.objects.exists())

    def test_created_at(self):
        """Contact Message must have an auto created at attribute"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Renato Padilha', str(self.obj))
