from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from notions.models import Category, Link


@login_required
def notions_main_page(request):          # если там, откуда пришел запрос,
    # if request.user.is_authenticated:  # юзер аутентифицирован, то все ок
    categories = Category.objects.all()
    links = Link.objects.all()
    print(links[0].category.icon.url)
    return render(request, 'notions/notions_main_page.html', {'categories': categories, 'links':links})
    # else:
    #     return redirect('login-page')  # иначе редирект на страницу авторизации


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

    return render(request, 'notions/notions_by_category.html', {'context': context, 'category':category})
