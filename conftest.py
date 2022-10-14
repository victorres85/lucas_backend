import pytest

from pytest_factoryboy import register

from api.factories import TeatroFactory, DiretorFactory, ProdutoraFactory

register(DiretorFactory)
register(ProdutoraFactory)
register(TeatroFactory)
