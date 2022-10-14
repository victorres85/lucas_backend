from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from .models import Teatro, AudioVisual, Director, Produtora
from .factories import TeatroFactory, DirectorFactory, ProdutoraFactory
from rest_framework.views import status
import json
from datetime import date

class Test_Director_Factory(APITestCase):
    client = APIClient()

    def setUp(self):
        self.nome = DirectorFactory(nome="Felini")
        
    def test_director(self):
        response = self.client.get('/director/'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        director_data = json.loads(response.content)[0]
        self.assertEqual(director_data['nome'], self.nome.__str__())

class Test_Teatro_ViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.director = DirectorFactory(nome="Almodovar")
        self.produtora = ProdutoraFactory(
            produtora  = 'produtora01', 
            nome_contato  = 'Joao Vicente' , 
            telefone  = 7518946014 ,
            # email  =  'jv@jv.com',
            endereco  = 'endereco 01, jardim 02'
            )
        self.teatro = TeatroFactory(
            )

    def test_teatro(self):
        response = self.client.get('/teatro/'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        teatro_data = json.loads(response.content)[0]
        print(teatro_data)

        self.assertEqual(teatro_data['titulo'], self.teatro.titulo)
        director_name = Director.objects.filter(id = int(teatro_data['director']))[0]
        self.assertEqual(director_name, self.teatro.director)
        self.assertEqual(teatro_data['video'], self.teatro.video)
        self.assertEqual(teatro_data['data'], self.teatro.data)
        self.assertEqual(teatro_data['ativo'], self.teatro.ativo)
        produtora_name = Produtora.objects.filter(id = int(teatro_data['produtora']))[0]
        self.assertEqual(produtora_name, self.teatro.produtora)
        self.assertEqual(teatro_data['personagem'], self.teatro.personagem)
