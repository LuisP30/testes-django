from django.test import TestCase
from ..models import Produto

class UserTestCase(TestCase):
    
    def setUp(self):
        Produto.objects.create(
            nome='Celular',
            valor='1000'
        )

    def test_usuario_criado_no_banco(self):
        celular = Produto.objects.get(nome='Celular')
        self.assertTrue(celular)

    def test_celular_e_instancia_de_produto(self):
        celular = Produto.objects.get(nome='Celular')
        self.assertIsInstance(celular, Produto)

        