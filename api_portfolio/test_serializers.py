from turtle import title
from django.test import TestCase
from .models import Trabalhos, Director, Produtora

from .factories import TeatroFactory, DirectorFactory, ProdutoraFactory
from .serializers import TrabalhosSerializer, DirectorSerializer, ProdutoraSerializer


class Test_TeatroSerializer(TestCase):
    def setUp(self) -> None:
        self.director = DirectorFactory(nome="Victor")
        self.produtora = ProdutoraFactory(
            produtora  = 'produtora01', 
            nome_contato  = 'Joao Vicente' , 
            telefone  = 7518946014 ,
            # email  =  'jv@jv.com',
            endereco  = 'endereco 01, jardim 02'
            )
        self.teatro = TeatroFactory()

        self.teatro_serializer = TeatroSerializer(self.teatro)

    def test_teatro_serializer(self):
        serializer_data = self.teatro_serializer.data
        print(serializer_data)
        self.assertEqual(serializer_data['titulo'], self.teatro.titulo)
        director_name = Director.objects.filter(id = int(serializer_data['director']))[0]
        self.assertEqual(director_name, self.teatro.director)
        self.assertEqual(serializer_data['video'], self.teatro.video)
        self.assertEqual(serializer_data['data'], self.teatro.data)
        self.assertEqual(serializer_data['ativo'], self.teatro.ativo)
        produtora_name = Produtora.objects.filter(id = int(serializer_data['produtora']))[0]
        self.assertEqual(produtora_name, self.teatro.produtora)
        self.assertEqual(serializer_data['personagem'], self.teatro.personagem)
       # self.assertEquals(serializer_data["titulo"], 100)
        # self.assertEquals(serializer_data["wine_name"], "mouse")
        # self.assertEquals(
        #     serializer_data["category"][0]["title"], "technology")