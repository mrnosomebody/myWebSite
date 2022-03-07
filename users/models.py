from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Person(User):
    wallet_address = models.CharField(max_length=255, blank=True, verbose_name='Wallet address')
    links_list = models.OneToOneField('LinksList', on_delete=models.CASCADE)

    def __str__(self):
        return super().username


class LinksList(models.Model):
    name = models.CharField(max_length=255, verbose_name="What's there")
    url = models.URLField(max_length=510, verbose_name='Link')
    category = TreeForeignKey('Category', on_delete=models.PROTECT, related_name='links', verbose_name='Category')

    def __str__(self):
        return self.name


class Category(MPTTModel):
    class MPTTMeta:
        order_insertion_by = ['name']

    name = models.CharField(max_length=255, unique=True, verbose_name='Category')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                            related_name='children', verbose_name='Parent category')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.parent is not None:
            return f'/notions/{self.slug}/'
            return f'/notions/{self.parent.slug}/{self.slug}/'
        return f'/notions/{self.slug}/'
