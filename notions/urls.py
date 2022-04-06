from django.urls import path, include

from JustInCase.views import login_
from .views import notions_main_page, detail, delete_link

urlpatterns = [
    path('', notions_main_page, name='notions'),
    path('login/', login_, name='login-page'),
    path('links/<int:link_id>/', delete_link, name='delete-link'),
    path('<slug>/', detail, name='notions-detail'),
    path('<slug>/<_slug>/', detail, name='notions-detail'),

]
