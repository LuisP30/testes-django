from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

def view_login(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('senha')
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('produtos:home')
    return render(request, 'login.html')

def view_cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('senha')
        User.objects.create_user(username=username, password=password)
        return redirect('usuarios:login')

    return render(request, 'cadastro.html')

def view_logout(request):
    logout(request)
    return redirect('usuarios:login')