from re import T
import factory
import datetime
import factory.fuzzy 

from .models import AudioVisual, Teatro, Publicidade, Locucao, Youtube, Produtora, Diretor


class DiretorFactory(factory.django.DjangoModelFactory):
    nome  = factory.Faker('pystr')
        
    class Meta:
        model = Diretor

class ProdutoraFactory(factory.django.DjangoModelFactory):
    produtora  = factory.Faker('pystr')
    nome_completo  = factory.Faker('pystr')
    telefone  = factory.Faker('pyint')
    email  = factory.Faker('pystr')
    endereco  = factory.Faker('pystr')

    class Meta:
        model = Produtora


class AudioVisualFactory(factory.django.DjangoModelFactory):
    titulo = factory.Faker('pystr')
    diretor = factory.LazyAttribute(DiretorFactory)
    video = factory.Faker('pystr')
    data = factory.LazyFunction(factory.fuzzy.FuzzyDate(datetime.date(1990, 6, 1), datetime.date.today()))
    ativo = factory.Faker([True, False])
    creado = factory.LazyFunction(factory.fuzzy.FuzzyDate(datetime.date(1990, 6, 1), datetime.date.today()))
    produtora = factory.LazyAttribute(ProdutoraFactory)

    @factory.post_generation
    def diretor(self, create, extracted, **kwargs):
        if not create:
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
    titulo = factory.Faker('pystr')
    diretor = factory.LazyAttribute(DiretorFactory)
    video = factory.Faker('pystr')
    data = factory.LazyFunction(factory.fuzzy.FuzzyDate(datetime.date(1990, 6, 1), datetime.date.today()))
    ativo = factory.Faker([True, False])
    creado = factory.LazyFunction(factory.fuzzy.FuzzyDate(datetime.date(1990, 6, 1), datetime.date.today()))
    produtora = factory.LazyAttribute(ProdutoraFactory)

    @factory.post_generation
    def diretor(self, create, extracted, **kwargs):
        if not create:
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
        model = Teatro


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
    diretor = factory.LazyAttribute(DiretorFactory)
    video  = factory.Faker('pystr')
    data = factory.LazyFunction(factory.fuzzy.FuzzyDate(datetime.date(1990, 6, 1), datetime.date.today()))
    ativo  = factory.Faker([True, False])
    creado = factory.LazyFunction(factory.fuzzy.FuzzyDate(datetime.date(1990, 6, 1), datetime.date.today()))
    produtora = factory.LazyAttribute(ProdutoraFactory)

    @factory.post_generation
    def diretor(self, create, extracted, **kwargs):
        if not create:
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
        model = Locucao

class YoutubeFactory(factory.django.DjangoModelFactory):
    titulo  = factory.Faker('pystr')
    video  = factory.Faker('pystr')
    descricao  = factory.Faker('pystr')
    data = factory.LazyFunction(factory.fuzzy.FuzzyDate(datetime.date(1990, 6, 1), datetime.date.today()))
    ativo  = factory.Faker([True, False])
    creado = factory.LazyFunction(factory.fuzzy.FuzzyDate(datetime.date(1990, 6, 1), datetime.date.today()))
    
    class Meta:
        model = Youtube