from django.test import TestCase
from django.contrib.auth.models import User

class UserTestCase(TestCase):
    
    def setUp(self):
        User.objects.create_user(
            username='usuario',
            password='1234'
        )
    
    def test_usuario_criado_no_banco(self):
        usuario = User.objects.get(username='usuario') # retorna apenas um objeto
        lista_usuarios = User.objects.filter(username='usuario') # retorna uma lista de objetos
        self.assertTrue(usuario)
        self.assertIn(usuario, lista_usuarios)
        
    def test_usuario_istancia_de_user(self):
        usuario = User.objects.get(username='usuario')
        self.assertIsInstance(usuario, User)
        
        
        