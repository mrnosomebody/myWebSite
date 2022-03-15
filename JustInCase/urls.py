from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path, include
from .views import index, login_, logout_

urlpatterns = [
    path('', index, name='home'),
    path('resume/', include('resume.urls')),
    path('notions/', include('notions.urls')),
    path('login/', login_, name='login-page'),
    path('logout/', logout_, name='logout-page'),
    path('admin/', admin.site.urls),
]
