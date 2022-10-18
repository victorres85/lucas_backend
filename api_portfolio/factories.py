from re import T
import factory
import datetime
import factory.fuzzy 
from faker import Faker
import random

trabalhos_list = [ 'Teatro', 'Audio Visual', 'Locucao','Youtube',  'Publicidade']

fake = Faker()

from .models import Trabalhos, Produtora, Director


class DirectorFactory(factory.django.DjangoModelFactory):
    nome  = fake.name()
        
    class Meta:
        model = Director

class ProdutoraFactory(factory.django.DjangoModelFactory):
    produtora  = fake.company()
    nome_contato  = fake.name()
    telefone  = fake.phone_number()
    email  = fake.ascii_company_email()
    endereco  = fake.address()

    class Meta:
        model = Produtora

class TrabalhosFactory(factory.django.DjangoModelFactory):
    trabalho = factory.Iterator(['Teatro', 'Audio Visual', 'Locucao','Youtube',  'Publicidade'])
    titulo = factory.Faker('pystr')
    director = factory.SubFactory(DirectorFactory)
    video = factory.Faker('pystr')
    data = fake.date()
    ativo = fake.boolean(chance_of_getting_true=50)
    creado = fake.date()
    produtora = factory.SubFactory(ProdutoraFactory)
    personagem = fake.name()

    @factory.post_generation
    def director(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for director in extracted:
                self.director.add(director)


    @factory.post_generation
    def produtora(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for produtora in extracted:
                self.produtora.add(produtora)


    class Meta:
        model = Trabalhos