from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import auth
from .forms import LoginForm


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
