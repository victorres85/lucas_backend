from rest_framework import serializers
from .models import AudioVisual, Diretor, Teatro, Produtora, Publicidade, Locucao, Youtube

class AudioVisualSerializer(serializers.ModelSerializer):
    diretor = DiretorSerializer(read_only = True, many=True)
    diretor_id = serializers.PrimaryKeyRelatedField(queryset = Diretor.objects.all(), write_only=True,  many=True)

    produtora = ProdutoraSerializer(read_only = True, many=True)
    produtora_id = serializers.PrimaryKeyRelatedField(queryset = Produtora.objects.all(), write_only=True,  many=True)
    
    def count_total(self, AudioVisula):
        total = AudioVisual.titulo.count()
        return total

    class Meta:
        model = AudioVisual
        fields = ('titulo', 'diretor', 'video', 'data', 'ativo', 'creado', 'produtora', 'total')


    def create(self, validated_data):
        diretor_data = validated_data.pop('diretor_id')
        produtora_data = validated_data.pop('produtora_id')

        audioVisual = AudioVisual.objects.create(**validated_data)
        for diretor in diretor_data:
            audioVisual.diretor.add(diretor)
        for produtora in produtora_data:
            audioVisual.produtora.add(produtora)


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
