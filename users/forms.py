from django.contrib.auth.forms import UserCreationForm
from django import forms
from users.models import Person


class UserRegisterForm(UserCreationForm):
    wallet_address = forms.CharField(max_length=80, required=False, help_text='Optional')

    class Meta:
        model = Person
        fields = ('username', 'email', 'password1', 'password2', "wallet_address")
