from django.shortcuts import render, get_object_or_404
from .models import Teatro, AudioVisual, Director, Produtora, Publicidade, Youtube, Locucao
from .serializers import TeatroSerializer, AudioVisualSerializer, DirectorSerializer, ProdutoraSerializer, PublicidadeSerializer, YoutubeSerializer, LocucaoSerializer
from  rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.

class TeatroViewSet(viewsets.ModelViewSet):
    queryset = Teatro.objects.all()
    serializer_class = (TeatroSerializer)


class AudioVisualViewSet(viewsets.ModelViewSet):
    queryset = AudioVisual.objects.all()
    serializer_class = (AudioVisualSerializer)


class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = (DirectorSerializer)


class ProdutoraViewSet(viewsets.ModelViewSet):
    '''
        only ViewSet for which I have used functions on
    '''
    def list(self, request):
        queryset = Produtora.objects.all()
        serializer = ProdutoraSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Produtora.objects.all()
        produtora = get_object_or_404(queryset, pk=pk)
        serializer = ProdutoraSerializer(produtora)
        return Response(serializer.data)
        

class LocucaoViewSet(viewsets.ModelViewSet):
    queryset = Locucao.objects.all()
    serializer_class = (LocucaoSerializer)


class YoutubeViewSet(viewsets.ModelViewSet):
    queryset = Youtube.objects.all()
    serializer_class = (YoutubeSerializer)


class PublicidadeViewSet(viewsets.ModelViewSet):
    queryset = Publicidade.objects.all()
    serializer_class = (PublicidadeSerializer)
