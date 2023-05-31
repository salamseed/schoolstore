from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/button')
        else:
            messages.info(request, "invalid credentials")
            return redirect('/loginapp/login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass1']
        c_password = request.POST['pass2']
        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already exists")
                return redirect('/loginapp/register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('/loginapp/login')
        else:
            messages.info(request, "password not matched")
            return redirect('/loginapp/register')

    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/loginapp/login')
