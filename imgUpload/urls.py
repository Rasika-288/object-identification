from django.contrib import admin
from django.urls import path, include

from .views import imageUpload, imageprocess


urlpatterns = [
    path('', imageUpload, name='home'),
    path('imageprocess', imageprocess, name='imageprocess'),
]


