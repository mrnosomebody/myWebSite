from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from notions.models import Category, Link, Person
from .forms import CategoryAddForm, LinkAddForm


@login_required
def notions_main_page(request):
    if request.method == 'POST':
        if 'addCategory' in request.POST:
            category_add_form = CategoryAddForm(request.POST)
            if category_add_form.is_valid():
                category = category_add_form.save(commit=False)
                creator = Person.objects.get(id=request.user.id)
                category.creator = creator
                category.slug = str(category.name).lower()
                category.save()
                return redirect('notions')
        elif 'addLink' in request.POST:
            link_add_form = LinkAddForm(request.POST)
            if link_add_form.is_valid():
                link_add_form.save()
                return redirect('notions')
    category_add_form = CategoryAddForm()
    link_add_form = LinkAddForm()
    categories = Category.objects.all()
    links = Link.objects.all()
    return render(request, 'notions/notions_main_page.html', {'categories': categories, 'links': links})


def detail(request, slug):
    context = []
    tmp_list = []
    category = Category.objects.get(slug=slug)
    context.append(category)
    for i in category.get_descendants(include_self=True):  # идем по дереву категорий и берем все ссылки, которые внутри
        links = Link.objects.filter(category=i)
        tmp_list.append(links)
    if len(tmp_list) > 0:
        context.append(tmp_list)
    return render(request, 'notions/notions_by_category.html', {'context': context, 'category': category})


def delete_link(request, link_id):
    link = Link.objects.get(id=link_id)
    link.delete()
    return redirect('notions')
