from django.db import models

# Create your models here.


class Director(models.Model):
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
    
class Book(models.Model):
    book = models.CharField(max_length=200)


class Trabalhos(models.Model):
    TRABALHO_CHOICES = [
    ('Teatro', 'Teatro'),
    ('Audio Visual', 'Audio Visual'),
    ('Locucao', 'Locucao'),
    ('Youtube', 'Youtube'),
    ('Publicidade', 'Publicidade'),
]
    trabalho = models.CharField(max_length = 12, choices = TRABALHO_CHOICES, default='Youtube')
    titulo = models.CharField(max_length = 200, unique=True)
    director = models.ManyToManyField(Director, blank=True)
    video = models.CharField(max_length = 500, unique=True, blank=True)
    data = models.DateField(blank=True)
    ativo = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    produtora = models.ManyToManyField(Produtora, blank=True)
    personagem = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='media/audiovisual/%y/%m/%d', null=True, blank=True)    

    def countTeatro(self):
        teatro = Trabalhos.objects.all().filter(trabalho='Teatro').count()
        return teatro

    def countAudioVisual(self):
        audioVisual = Trabalhos.objects.all().filter(trabalho='Audio Visual').count()
        return audioVisual

    def countYoutube(self):
        youtube = Trabalhos.objects.all().filter(trabalho='Youtube').count()
        return youtube

    def countPublicidade(self):
        publicidade = Trabalhos.objects.all().filter(trabalho='Publicidade').count()
        return publicidade

    def countLocucao(self):
        locucao = Trabalhos.objects.all().filter(trabalho='Locucao').count()
        return locucao


class Album(models.Model):
    image = models.ImageField(upload_to='media/album/%y/%m/%d', blank=True)
    trabalhos = models.ForeignKey(Trabalhos, on_delete=models.CASCADE, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return str(self.image)[21:]
