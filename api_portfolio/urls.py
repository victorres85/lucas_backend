from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import TrabalhosViewSet, ProdutoraViewSet, DirectorViewSet


router = routers.DefaultRouter()
router.register(r"trabalhos", TrabalhosViewSet, basename='trabalhos-list')
router.register(r"produtora", ProdutoraViewSet, basename='produtora')
router.register(r"director", DirectorViewSet, basename='director')

app_name = 'api_portfolio'

urlpatterns = [
    path('', include(router.urls)),

]
