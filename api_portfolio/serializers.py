from rest_framework import serializers
from .models import  Trabalhos, Director, Produtora, Album

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('id','nome')
        
class TrabalhosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabalhos
        fields = ('titulo', 'director', 'video', 'image', 'data', 'ativo', 'creado', 'produtora', 'personagem', 'countTeatro')


class ProdutoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtora
        fields = ('produtora', 'nome_completo', 'telefone', 'email', 'endereco')
