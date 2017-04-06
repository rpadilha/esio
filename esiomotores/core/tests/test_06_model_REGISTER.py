from datetime import datetime
from django.test import TestCase
from esiomotores.core.models import CustomerMKT


class ContactModelTest(TestCase):
    def setUp(self):
        self.obj = CustomerMKT(
            name='Renato Padilha',
            email='tonare@gmail.com'
        )
        self.obj.save()

    def test_create (self):
        self.assertTrue(CustomerMKT.objects.exists())

    def test_created_at(self):
        """Customer register must have an auto created at attribute"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Renato Padilha', str(self.obj))
