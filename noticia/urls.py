from django.urls import path
from .views import lista_noticia,pre_cadastro_noticia

urlpatterns = [
    path('noticias/', lista_noticia, name='noticias'),
    path('noticias/pre_cadastro/', pre_cadastro_noticia, name='pre_cadastro_noticia'),
]