from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from django.contrib.auth.models import User


class ViewsTesteCase(TestCase):

    def setUp(self):
        self.usuario = User.objects.create_user(
            username='luis',
            password='1234'
        )
        self.client = Client()
        self.url = reverse('usuarios:login')

    def test_requisicao_get_login_status_code_200(self):
        response = self.client.get(f'{self.url}') # Realizando requisição do tipo get
        self.assertEqual(response.status_code, 200)

    def test_template_usado_login(self):
        response = self.client.get(f'{self.url}')
        self.assertTemplateUsed(response, 'login.html')
        
    def test_requisicao_post_login_status_code_302(self):
        response = self.client.post(f'{self.url}', {'user': 'luis', 'senha': '1234'})
        # Se o usuário existe no banco de dados e tem o login realizado, ele é redirecionado (status 302) para a página home
        self.assertEqual(response.status_code, 302)