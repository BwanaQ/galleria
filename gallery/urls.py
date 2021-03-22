from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='gallery-home'),
    path('location/<str:location>', views.image_location, name='location'),
    path('category/<str:category>', views.image_category, name='category'),
    path('search/', views.search_image, name='search')
]
