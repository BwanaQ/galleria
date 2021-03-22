from django.shortcuts import render
from django.http import HttpResponse

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
    return render(request, 'gallery/home.html')


def about(request):
    return render(request, 'gallery/about')
