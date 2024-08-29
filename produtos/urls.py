from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.home, name='home'),
    path('produto/create/', views.cria_produto, name='cria_produto'),
    path('produto/delete/<int:id>', views.remove_produto, name='remove_produto'),
]