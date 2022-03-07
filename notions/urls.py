from django.urls import path, include
from .views import notions_main_page, detail

urlpatterns = [
    path('', notions_main_page, name='notions'),
    path('<slug>/', detail, name='notions-detail'),
    path('<slug>/<_slug>/', detail, name='notions-detail'),
    path('accounts/', include('django.contrib.auth.urls')),
]