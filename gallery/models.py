from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations

    def __str__(self):
        return self.name

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(name=value)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        verbose_name_plural = "cities"
        return self.name

    class Meta:
        ordering = ['name']

    @classmethod
    def get_categories(cls):
        categories = Category.objects.all()
        return categories

    @classmethod
    def update_category(cls, id, value):
        cls.objects.filter(id=id).update(name=value)

    def save_category(self):
        self.save()

    def delete_category(self):
        Category.objects.filter(id=self.pk).delete()


class Image(models.Model):
    image_url = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['timestamp']

    @classmethod
    def filter_by_location(cls, location):
        image_location = Image.objects.filter(location__name=location).all()
        return image_location

    @classmethod
    def filter_by_category(cls, category):
        image_category = Image.objects.filter(category__name=category).all()
        return image_category

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image

    @classmethod
    def search_by_category(cls, category):
        images = cls.objects.filter(name__icontains=category)
        return images
