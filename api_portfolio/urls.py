from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import TeatroViewSet, AudioVisualViewSet, LocucaoViewSet, YoutubeViewSet, ProdutoraViewSet, PublicidadeViewSet, DirectorViewSet


router = routers.DefaultRouter()
router.register(r"teatro", TeatroViewSet, basename='teatro-list')
router.register(r"audioVisual", AudioVisualViewSet, basename='audioVisual')
router.register(r"locucao", LocucaoViewSet, basename='locucao')
router.register(r"youtube", YoutubeViewSet, basename='youtube')
router.register(r"produtora", ProdutoraViewSet, basename='produtora')
router.register(r"publicidade", PublicidadeViewSet, basename='publicidade')
router.register(r"director", DirectorViewSet, basename='director')

app_name = 'api_portfolio'

urlpatterns = [
    path('', include(router.urls)),

]
