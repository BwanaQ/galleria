from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='gallery-home'),
    path('images/<int:image_id>/', views.image, name='gallery-image'),
    path('location/<str:location>', views.image_location,
         name='gallery-image-location'),
    path('category/<str:category>', views.image_category,
         name='gallery-image-category'),
    path('search/', views.search_images, name='gallery-search')
]
