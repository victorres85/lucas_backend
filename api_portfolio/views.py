from django.shortcuts import render, get_object_or_404
from .models import Director, Produtora, Trabalhos
from .serializers import DirectorSerializer, ProdutoraSerializer, TrabalhosSerializer
from  rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.

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
        


class TrabalhosViewSet(viewsets.ModelViewSet):
    queryset = Trabalhos.objects.all()
    serializer_class = (TrabalhosSerializer)
