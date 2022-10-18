from turtle import title
from django.test import TestCase
from .models import Trabalhos, Director, Produtora

from .factories import TrabalhosFactory, DirectorFactory, ProdutoraFactory
from .serializers import TrabalhosSerializer, DirectorSerializer, ProdutoraSerializer


class Test_TrabalhosSerializer(TestCase):
    def setUp(self):
        self.director = DirectorFactory()
        self.produtora = ProdutoraFactory(
            produtora  = 'produtora01', 
            nome_contato  = 'Joao Vicente' , 
            telefone  = 7518946014 ,
            email  =  'jv@jv.com',
            endereco  = 'endereco 01, jardim 02'
            )
        
        self.trabalho = TrabalhosFactory()

        self.trabalho_serializer = TrabalhosSerializer(self.trabalho)

    def test_trabalho_serializer(self):
        serializer_data = self.trabalho_serializer.data
        print(serializer_data)
        self.assertEqual(serializer_data['trabalho'], self.trabalho.trabalho)
        self.assertEqual(serializer_data['titulo'], self.trabalho.titulo)
        self.assertEqual(serializer_data['video'], self.trabalho.video)
        self.assertEqual(serializer_data['data'], self.trabalho.data)
        self.assertEqual(serializer_data['ativo'], self.trabalho.ativo)
        self.assertEqual(serializer_data['personagem'], self.trabalho.personagem)
