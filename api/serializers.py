from rest_framework import serializers
from .models import AudioVisual, Diretor, Teatro, Produtora, Publicidade, Locucao, Youtube

class AudioVisualSerializer(serializers.ModelSerializer):
    def count_total(self, AudioVisula):
        total = AudioVisual.titulo.count()
        return total

    class Meta:
        model = AudioVisual
        fields = ('titulo', 'diretor', 'video', 'data', 'ativo', 'creado', 'produtora', 'total')


class DiretorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diretor
        fields = ('nome')
        
class TeatroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teatro
        fields = ('titulo', 'diretor', 'video', 'data', 'ativo', 'creado', 'produtora')


class ProdutoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtora
        fields = ('produtora', 'nome_completo', 'telefone', 'email', 'endereco')

class PublicidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicidade 
        fields = ('empresa', 'video', 'data', 'ativo', 'creado')


class LocucaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locucao
        fields = ('titulo', 'diretor', 'video', 'data', 'ativo', 'creado', 'produtora')


class YoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Youtube
        fields = ('titulo', 'video', 'descricao', 'data', 'ativo', 'creado')
