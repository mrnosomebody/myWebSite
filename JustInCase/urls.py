from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index),
    path('resume/', include('resume.urls')),
    path('notions/', include('notions.urls')),
    path('admin/', admin.site.urls),
]
