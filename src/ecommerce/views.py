from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import auth
from .forms import LoginForm
from django.contrib.auth import get_user_model
from ecommerce.forms import RegisterForm

User = get_user_model()


def home(request):
    context = {'title': 'Home'}
    return render(request, "home.html", context)


def login(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            print('error')

    return render(request, 'auth/login.html', {'form': form})


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {'form': form}

    if form.is_valid():
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        User.objects.create_user(username, email, password)
        return redirect('/login')

    return render(request, "auth/register.html", context)