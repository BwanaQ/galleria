from django.test import TestCase
from .models import Image, Category, Location
from django.contrib.auth.models import User
from django.utils import timezone

# Create your tests here.


class ImageTestClass(TestCase):
    # set up method

    def setUp(self):
        self.location = Location(name='Kitui')
        self.location.save_location()

        self.category = Category(name='family')
        self.category.save_category()

        self.user = User(id=1, is_superuser=False, password="pass1234", last_login=timezone.now(
        ), username="testuser2", email="testuser@gmail.com", is_active=True, first_name="Test", last_name="User", is_staff=False, date_joined=timezone.now())
        self.user.save()

        self.image = Image(id=1, name='image', description='this is a test image', timestamp=timezone.now(
        ), author=self.user, location=self.location, category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_image(self):
        self.image.save_image()
        after = Image.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_image(self):
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_image(self):
        self.image.save_image()
        self.image.update_image(self.image.id, 'photos/test.jpg')
        changed_img = Image.objects.filter(image='photos/test.jpg')
        self.assertTrue(len(changed_img) > 0)

    def test_get_image_by_id(self):
        found_image = self.image.get_image_by_id(self.image.id)
        image = Image.objects.filter(id=self.image.id)
        self.assertTrue(found_image, image)

    def test_search_image_by_location(self):
        self.image.save_image()
        found_images = self.image.filter_by_location(location='Nairobi')
        self.assertTrue(len(found_images) == 1)

    def test_search_image_by_category(self):
        category = 'family'
        found_img = self.image.search_by_category(category)
        self.assertTrue(len(found_img) > 0)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()


class TestLocation(TestCase):
    def setUp(self):
        self.location = Location(name='Nairobi')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)

    def test_get_locations(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)

    def test_update_location(self):
        new_location = 'Machakos'
        self.location.update_location(self.location.id, new_location)
        changed_location = Location.objects.filter(name='Machakos')
        self.assertTrue(len(changed_location) > 0)

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)


class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name='family')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)
