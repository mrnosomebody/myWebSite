from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path, include
from .views import index, login_, logout_, signup

urlpatterns = [
    path('', index, name='home'),
    path('bookmarks/', include('bookmarks.urls')),
    path('login/', login_, name='login-page'),
    path('logout/', logout_, name='logout-page'),
    path('signup/', signup, name='signup-page'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
