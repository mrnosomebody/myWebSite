import requests
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from users.models import Person


class Link(models.Model):
    name = models.CharField(max_length=255, verbose_name="What's there")
    url = models.URLField(max_length=510, verbose_name='Link')
    category = TreeForeignKey('Category', on_delete=models.PROTECT, related_name='links', verbose_name='Category')


    def __str__(self):
        return self.name


class Category(MPTTModel):
    class MPTTMeta:
        order_insertion_by = ['name']

    name = models.CharField(max_length=255, verbose_name='Category')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, blank=True, null=True,
                            related_name='children', verbose_name='Parent category')
    slug = models.SlugField(unique=True)
    creator = models.ForeignKey(Person, on_delete=models.PROTECT)
    icon = models.ImageField(upload_to='media/', blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/notions/{self.slug}/'
