from django.shortcuts import render
from .models import Teatro, AudioVisual, Diretor, Produtora, Publicidade, Youtube, Locucao
from api.serializers import TeatroSerializer, AudioVisualSerializer, DiretorSerializer, ProdutoraSerializer, PublicidadeSerializer, YoutubeSerializer, LocucaoSerializer
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


class DiretorViewSet(viewsets.ModelViewSet):
    queryset = Diretor.objects.all()
    serializer_class = (DiretorSerializer)


class ProdutoraViewSet(viewsets.ModelViewSet):
    queryset = Produtora.objects.all()
    serializer_class = (ProdutoraSerializer)


class LocucaoViewSet(viewsets.ModelViewSet):
    queryset = Locucao.objects.all()
    serializer_class = (LocucaoSerializer)


class YoutubeViewSet(viewsets.ModelViewSet):
    queryset = Youtube.objects.all()
    serializer_class = (YoutubeSerializer)


class PublicidadeViewSet(viewsets.ModelViewSet):
    queryset = Publicidade.objects.all()
    serializer_class = (PublicidadeSerializer)
