from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import TeatroViewSet, AudioVisualViewSet, LocucaoViewSet, YoutubeViewSet, ProdutoraViewSet, PublicidadeViewSet, DiretorViewSet

router = routers.DefaultRouter()
router.register("teatro", TeatroViewSet)
router.register("audioVisual", AudioVisualViewSet)
router.register("locucao", LocucaoViewSet)
router.register("youtube", YoutubeViewSet)
router.register("produtora", ProdutoraViewSet)
router.register("publicidade", PublicidadeViewSet)
router.register("diretor", DiretorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('audioVisual', include(router.urls)),
    # path('locucao', include(router.urls)),
    # path('youtube', include(router.urls)),
    # path('produtora', include(router.urls)),
    # path('publicidade', include(router.urls)),
    # path('diretor', include(router.urls)),
]
