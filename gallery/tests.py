from django.test import TestCase
from .models import Image, Category, Location
from django.contrib.auth.models import User

# Create your tests here.


class ImageTestClass(TestCase):
    # set up method
    def setUp(self):
        self.image = Image(name="Test Image")
