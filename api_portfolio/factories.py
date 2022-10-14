from re import T
import factory
import datetime
import factory.fuzzy 
from faker import Faker

fake = Faker()

from .models import AudioVisual, Teatro, Publicidade, Locucao, Youtube, Produtora, Director


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


class AudioVisualFactory(factory.django.DjangoModelFactory):
    titulo = factory.Faker('pystr')
    director = factory.SubFactory(DirectorFactory)
    video = factory.Faker('pystr')
    data = factory.LazyFunction(factory.fuzzy.FuzzyDate(datetime.date(1990, 6, 1), datetime.date.today()))
    ativo = factory.Faker([True, False])
    creado = factory.LazyFunction(factory.fuzzy.FuzzyDate(datetime.date(1990, 6, 1), datetime.date.today()))
    produtora = factory.SubFactory(ProdutoraFactory)

    @factory.post_generation
    def director(self, create, extracted, **kwargs):
        if not create:
            DirectorFactory.create()
            return
        if extracted:
            for diretor in extracted:
                self.diretor.add(diretor)


    @factory.post_generation
    def produtora(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for produtora in extracted:
                self.produtora.add(produtora)
                

    class Meta:
        model = AudioVisual    


class TeatroFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Teatro

    titulo = factory.Faker('pystr')
    director = factory.SubFactory(DirectorFactory)
    video = factory.Faker('pystr')
    data = fake.date()
    ativo = fake.boolean(chance_of_getting_true=50)
    creado = fake.date()
    produtora = factory.SubFactory(ProdutoraFactory)
    personagem = fake.name()

    # @factory.post_generation
    # def diretor(self, create, extracted, **kwargs):
    #     if not create:
    #         return
    #     if extracted:
    #         for diretor in extracted:
    #             self.diretor.add(diretor)


    # @factory.post_generation
    # def produtora(self, create, extracted, **kwargs):
    #     if not create:
    #         return
    #     if extracted:
    #         for produtora in extracted:
    #             self.produtora.add(produtora)


class PublicidadeFactory(factory.django.DjangoModelFactory):
    empresa = factory.Faker('pystr')
    video = factory.Faker('pystr')
    data = factory.LazyFunction(factory.fuzzy.FuzzyDate(datetime.date(1990, 6, 1), datetime.date.today()))
    ativo = factory.Faker([True, False])
    creado = factory.LazyFunction(factory.fuzzy.FuzzyDate(datetime.date(1990, 6, 1), datetime.date.today()))
    

    class Meta:
        model = Publicidade

class LocucaoFactory(factory.django.DjangoModelFactory):
    titulo  = factory.Faker('pystr')
    director = factory.SubFactory(DirectorFactory)
    video  = factory.Faker('pystr')
    data = factory.LazyFunction(factory.fuzzy.FuzzyDate(datetime.date(1990, 6, 1), datetime.date.today()))
    ativo  = factory.Faker([True, False])
    creado = factory.LazyFunction(factory.fuzzy.FuzzyDate(datetime.date(1990, 6, 1), datetime.date.today()))
    produtora = factory.SubFactory(ProdutoraFactory)

    # @factory.post_generation
    # def diretor(self, create, extracted, **kwargs):
    #     if not create:
    #         return
    #     if extracted:
    #         for diretor in extracted:
    #             self.diretor.add(diretor)


    # @factory.post_generation
    # def produtora(self, create, extracted, **kwargs):
    #     if not create:
    #         return
    #     if extracted:
    #         for produtora in extracted:
    #             self.produtora.add(produtora)

    class Meta:
        model = Locucao

class YoutubeFactory(factory.django.DjangoModelFactory):
    titulo  = factory.Faker('pystr')
    video  = factory.Faker('pystr')
    descricao  = fake.text()
    data = factory.LazyFunction(factory.fuzzy.FuzzyDate(datetime.date(1990, 6, 1), datetime.date.today()))
    ativo  = factory.Faker([True, False])
    creado = factory.LazyFunction(factory.fuzzy.FuzzyDate(datetime.date(1990, 6, 1), datetime.date.today()))
    
    class Meta:
        model = Youtube