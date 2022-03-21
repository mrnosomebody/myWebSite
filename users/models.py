from django.contrib.auth.models import User
from django.db import models


class Person(User):
    wallet_address = models.CharField(max_length=255, blank=True, null=True, verbose_name='Wallet address')

    def __str__(self):
        return super().username
