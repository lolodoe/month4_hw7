from django.http import HttpResponse
from django.shortcuts import render, redirect
from users.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from posts.views import get_user_from_request
# Create your views here.


def register(request):
    if request.method == 'GET':
        return render(request, 'users/register.html', context={'form': RegisterForm})
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password'),
                email=form.cleaned_data.get('email'),
                is_active=True,
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name')
            )
            return redirect('/users/login/')
        else:
            return render(request, 'users/register.html', context={'form': form})


def login_(request):
    if request.method == 'GET':
        return render(request, 'users/login.html', context={'form': LoginForm})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user:
                login(request, user)
                return redirect('/')
        else:
            return render(request, 'users/login.html', context={'form': form})


def logout_(request):
    if request.method == 'GET':
        logout(request)
        return redirect('/')


def users(request, user_id):
    if request.method == 'GET':
        try:
            return render(request, 'users/all_users.html', context={'user': User.objects.get(id=user_id)})
        except:
            return HttpResponse("Такого пользователя нету")


def personal_info(request):
    if request.method == 'GET':
        if get_user_from_request(request):
            return render(request, 'users/personal_info.html', context={'user': request.user})
        else:
            return redirect('/')


def set_password(request, id):
    if request.method == 'GET':
        return render(request, 'users/set_password.html', context={
            'form': SetPassForm,
            'id': id
        })
    elif request.method == 'POST':
        form = SetPassForm(request.POST)
        user = User.objects.get(id=id)
        if form.is_valid():
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return redirect('/')
        else:
            return render(request, 'users/set_password.html', context={
                'form': SetPassForm,
                'id': id
            })