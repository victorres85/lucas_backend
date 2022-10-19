from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from .models import Director, Produtora
from .factories import DirectorFactory, ProdutoraFactory, TrabalhosFactory
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

class Test_Trabalhos_ViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.director = DirectorFactory()
        self.produtora = ProdutoraFactory()
        self.trabalho = TrabalhosFactory()

    def test_trabalho(self):
        response = self.client.get('/trabalhos/'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        trabalho_data = json.loads(response.content)[0]
 
        self.assertEqual(trabalho_data['titulo'], self.trabalho.titulo)
        self.assertEqual(trabalho_data['video'], self.trabalho.video)
        self.assertEqual(trabalho_data['data'], self.trabalho.data)
        self.assertEqual(trabalho_data['ativo'], self.trabalho.ativo)
        self.assertEqual(trabalho_data['personagem'], self.trabalho.personagem)
