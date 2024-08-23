from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth import authenticate, login

def login(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('senha')
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(usuario)
            return redirect('produtos:home')
    return render(request, 'login.html')

def cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('senha')
        Usuario.objects.create_user(username=username, password=password)
        return redirect('usuarios:login')

    return render(request, 'cadastro.html')