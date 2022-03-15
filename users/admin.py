from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Person, Category, Link


admin.site.register(Person)


class CategoryAdmin(DjangoMpttAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Link)

