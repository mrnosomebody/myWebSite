from django.urls import path
from .views import notions_main_page

urlpatterns = [
    path('notions/', notions_main_page)
]