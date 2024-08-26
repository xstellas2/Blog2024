from django.urls import path
from .views import lista_noticia,cadastrar_noticias

urlpatterns = [
    path('noticias/', lista_noticia, name='noticias'),
]