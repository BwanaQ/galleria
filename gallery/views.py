from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Location, Category, Image

# Create your views here.


def home(request):
    context = {
        'images': Image.objects.all(),
        'locations': Location.get_locations(),
        'categories': Category.get_categories()
    }
    return render(request, 'gallery/home.html', context)


def image_location(request, location):
    images = Image.filter_by_location(location)
    return render(request, 'gallery/home.html', {'images': images})


def image_category(request, category):
    images = Image.filter_by_category(category)
    return render(request, 'gallery/home.html', {'images': images})


def search_image(request):
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        images = Image.search_by_category(search_term)
        message = f'{search_term}'
        return render(request, 'gallery/home.html', {'message': message, "images": images})

    else:
        message = "No images found"
        return render(request, 'gallery/search_image.html', {'messages': message})


def image(request, image_id):
    try:
        image = Image.objects.get(id=image_id)
    except DoesNotExist:
        raise Http404()
    return(request, 'gallery/image.html', {'image': image})
