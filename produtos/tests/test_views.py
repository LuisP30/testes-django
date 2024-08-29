from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Produto

class ViewsTesteCase(TestCase):

    def setUp(self):
        # Cria usuário
        self.usuario = User.objects.create_user(
            username='user',
            password='1234'
        )
        
        self.client = Client() # Para fazer requisição
        self.client.login(username='user', password='1234') # Autenticando o usuário de teste
        self.url = reverse('produtos:home') # Pegando o caminho da URL de Home

    def test_requisicao_get_home_status_code_200(self):
        response = self.client.get(f'{self.url}') # Realizando requisição do tipo get
        self.assertEqual(response.status_code, 200)

    def test_template_usado_home(self):
        response = self.client.get(f'{self.url}')
        self.assertTemplateUsed(response, 'home.html') # Este HTML só é acessado por usuários que estão autenticados
        
    def test_cria_produto(self):
        self.client.post(f'{reverse('produtos:cria_produto')}', {'nome': 'Celular', 'valor': 1000})
        produto = Produto.objects.get(nome='Celular')
        self.assertTrue(produto)
        
    def test_cria_produto_status_code_302(self):
        response = self.client.get(f'{reverse('produtos:cria_produto')}') # Realizando requisição do tipo get
        self.assertEqual(response.status_code, 302)