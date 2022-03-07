from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView

from users.models import Category, LinksList


@login_required
def notions_main_page(request):
    categories = Category.objects.all()
    return render(request, 'notions/notions_main_page.html', {'categories':categories})

def detail(request, slug):
    context = []

    category = Category.objects.get(slug=slug)
    context.append(category)

    tmp_list = []
    for i in category.get_descendants(include_self=True):
        links = LinksList.objects.filter(category=i)
        tmp_list.append(links)
    if len(tmp_list) > 0:
        context.append(tmp_list)

    return render(request, 'notions/notions_by_category.html', {'context': context})
