from django.test import TestCase
from ..form import ProdutoForm
from django.http import HttpRequest

class FormsTestCase(TestCase):
    
    def setUp(self):
        self.form = ProdutoForm()
        
    def test_campos_form_produto(self):
        # Verificando se o form possui os campos do model
        self.assertIn('nome', self.form.fields)
        self.assertIn('valor', self.form.fields)
        
    def test_form_produto_valido(self):
        request = HttpRequest()
        request.POST = {
            "nome": 'Camisa',
            "valor": 55
        }
        form = ProdutoForm(request.POST)
        self.assertTrue(form.is_valid())