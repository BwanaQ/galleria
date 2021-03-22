from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Location, Category, Image

# Create your views here.


def home(request):
    context = {
        'images': Image.objects.all()
    }
    return render(request, 'gallery/home.html', context)


def about(request):
    return render(request, 'gallery/about')


def image(request, image_id):
    try:
        image = Image.objects.get(id=article_id)
    except DoesNotExist:
        raise Http404()
    return(request, 'gallery/image.html', {'image': image})
