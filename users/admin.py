from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Person


admin.site.register(Person)




