from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Produto

@login_required(login_url=settings.LOGIN_URL)
def home(request):
    produtos = Produto.objects.all()
    return render(request, 'home.html', context={
        'produtos': produtos,
    })

def remove_produto(request, id):
    produto = Produto.objects.get(id=id)
    print(produto)
    if produto:
        produto.delete()
    return redirect(f'{reverse('produtos:home')}')
    

def cria_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        valor = request.POST.get('valor')
        Produto.objects.create(nome=nome, valor=valor)
        return redirect(f'{reverse('produtos:home')}')
    return redirect(f'{reverse('produtos:home')}')