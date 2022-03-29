from django.urls import path, include
from .views import resume
urlpatterns = [
    path('', resume, name='resume'),
]

