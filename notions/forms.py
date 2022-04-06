from django import forms
from .models import Category, Link


class CategoryAddForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'parent')


class LinkAddForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = '__all__'
