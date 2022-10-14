from rest_framework import serializers
from .models import AudioVisual, Director, Teatro, Produtora, Publicidade, Locucao, Youtube

class AudioVisualSerializer(serializers.ModelSerializer):
    # diretor = DiretorSerializer(read_only = True, many=True)
    # diretor_id = serializers.PrimaryKeyRelatedField(queryset = Diretor.objects.all(), write_only=True,  many=True)

    # produtora = ProdutoraSerializer(read_only = True, many=True)
    # produtora_id = serializers.PrimaryKeyRelatedField(queryset = Produtora.objects.all(), write_only=True,  many=True)
    
    # def count_total(self, AudioVisula):
    #     total = AudioVisual.titulo.count()
    #     return total

    class Meta:
        model = AudioVisual
        fields = ('titulo', 'director', 'video', 'image', 'data', 'ativo', 'creado', 'produtora')


    def create(self, validated_data):
        director_data = validated_data.pop('director_id')
        produtora_data = validated_data.pop('produtora_id')

        audioVisual = AudioVisual.objects.create(**validated_data)
        for director in director_data:
            audioVisual.director.add(director)
        for produtora in produtora_data:
            audioVisual.produtora.add(produtora)


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('id','nome')
        
class TeatroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teatro
        fields = ('titulo', 'director', 'video', 'image', 'data', 'ativo', 'creado', 'produtora', 'personagem')


class ProdutoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtora
        fields = ('produtora', 'nome_completo', 'telefone', 'email', 'endereco')

class PublicidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicidade 
        fields = ('empresa', 'video', 'image', 'data', 'ativo', 'creado')


class LocucaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locucao
        fields = ('titulo', 'director', 'video', 'image', 'data', 'ativo', 'creado', 'produtora')


class YoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Youtube
        fields = ('titulo', 'video', 'image', 'descricao', 'data', 'ativo', 'creado')
