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
    return render(request, 'location.html', {'location_images': images})


def image_category(request, category):
    images = Image.filter_by_category(category)
    return render(request, 'category.html', {'category_images': images})


def search_image(request):
    if 'imagesearch' in request.GET and request.GET['imagesearch']:
        category = request.GET.get('imagesearch')
        searched_images = Image.search_by_category(category)
        message = f'{category}'
        return render(request, 'search_image.html', {'message': message, "image": searched_images})

    else:
        message = "No images found"
        return render(request, 'search_image.html', {'messages': message})


def about(request):
    return render(request, 'gallery/about')


def image(request, image_id):
    try:
        image = Image.objects.get(id=article_id)
    except DoesNotExist:
        raise Http404()
    return(request, 'gallery/image.html', {'image': image})
