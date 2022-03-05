from django.shortcuts import render

def notions_main_page(request):
    return render(request, 'index.html')
