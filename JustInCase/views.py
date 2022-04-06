from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, redirect
from users.forms import UserRegisterForm


def index(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        print(subject, email, message)
    return render(request, 'main/index.html')


def login_(request):
    next_ = request.GET.get('next', '')  # @login_required отдает next(куда идти далее)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if next_ != '':
                return redirect(next_)  # туда и идем
            return redirect('home')
        else:
            return redirect(request.get_full_path())
    return render(request, 'auth/login.html')


def logout_(request):
    next_ = request.GET.get('next', '')
    logout(request)
    if next_ != '':
        return redirect(next_)  # туда и идем
    return redirect('home')


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'auth/sign_up.html', {'form': form})
