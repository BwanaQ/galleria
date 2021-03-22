from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='gallery-home'),
    path('image/<int:id>', views.image, name='gallery-image'),
    path('about/', views.about, name='gallery-about'),
]
