from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import TeatroViewSet, AudioVisualViewSet, LocucaoViewSet, YoutubeViewSet, ProdutoraViewSet, PublicidadeViewSet, DiretorViewSet

router = routers.SimpleRouter()
router.register("teatro", TeatroViewSet, basename='teatro')
router.register("audioVisual", AudioVisualViewSet, basename='audioVisual')
router.register("locucao", LocucaoViewSet, basename='locucao')
router.register("youtube", YoutubeViewSet, basename='youtube')
router.register("produtora", ProdutoraViewSet, basename='produtora')
router.register("publicidade", PublicidadeViewSet, basename='publicidade')
router.register("diretor", DiretorViewSet, basename='diretor')

urlpatterns = [
    path('', include(router.urls)),

]
