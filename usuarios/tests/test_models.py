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
        self.assertTrue(usuario)

    def test_usuario_instancia_de_user(self):
        usuario = User.objects.get(username='usuario')
        self.assertIsInstance(usuario, User)

        
        