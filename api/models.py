from email.policy import default
from django.db import models

# Create your models here.


class Diretor(models.Model):
    nome = models.CharField(max_length = 200, unique=True)

    def __str__(self):
        return self.nome

class Produtora(models.Model):
    produtora = models.CharField(max_length = 200, unique=True)
    nome_contato = models.CharField(max_length = 200, unique=True, blank=True)
    telefone = models.CharField(max_length = 20, unique=True, blank=True)
    email = models.EmailField(blank=True)
    endereco = models.CharField(max_length = 200, unique=True, blank=True)


    def __str__(self):
        return self.produtora

class AudioVisual(models.Model):
    titulo = models.CharField(max_length = 200, unique=True)
    diretor = models.ManyToManyField(Diretor)
    video = models.CharField(max_length = 500, unique=True, blank=True)
    data = models.DateField(blank=True)
    ativo = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    produtora = models.ManyToManyField(Produtora, blank=True)
    #fotos
    def __str__(self):
        return self.titulo
    

class Teatro(models.Model):
    titulo = models.CharField(max_length = 200, unique=True)
    diretor = models.ManyToManyField(Diretor, blank=True)
    video = models.CharField(max_length = 500, unique=True, blank=True)
    data = models.DateField()
    ativo = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    produtora = models.ManyToManyField(Produtora, blank=True)

    Personagem = models.CharField(max_length = 200, unique=True)
    #fotos
    def __str__(self):
        return self.titulo

class Locucao(models.Model):
    titulo = models.CharField(max_length = 200, unique=True)
    diretor = models.ManyToManyField(Diretor, blank=True)
    video = models.CharField(max_length = 500, unique=True, blank=True)
    data = models.DateField()
    ativo = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    produtora = models.ManyToManyField(Produtora, blank=True)

    def __str__(self):
        return self.titulo

class Youtube(models.Model):
    titulo = models.CharField(max_length = 200, unique=True)
    video = models.CharField(max_length = 500, unique=True, blank=True)
    descricao = models.TextField(blank=True)
    data = models.DateField()
    ativo = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.titulo


class Publicidade(models.Model):
    empresa = models.CharField(max_length = 200, unique=True)
    video = models.CharField(max_length = 500, unique=True, blank=True)
    data = models.DateField()
    ativo = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.empresa