
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('imgUploads/', include('imgUpload.urls')),
    path('admin/', admin.site.urls),
]




