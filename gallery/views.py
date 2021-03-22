from django.shortcuts import render
from django.http import HttpResponse
from .models import Location, Category, Image

# Create your views here.
images = [
    {
        'image_url': '#',
        'name': 'Test Image',
        'description': 'Testing description',
        'location': 'Kitui',
        'category': 'excursion'
    },
    {
        'image_url': '#',
        'name': 'Test Image',
        'description': 'Testing description',
        'location': 'Kitui',
        'category': 'excursion'
    },
    {
        'image_url': '#',
        'name': 'Test Image',
        'description': 'Testing description',
        'location': 'Kitui',
        'category': 'excursion'
    },
]


def home(request):
    context = {
        'images': Image.objects.all()
    }
    return render(request, 'gallery/home.html', context)


def about(request):
    return render(request, 'gallery/about')
