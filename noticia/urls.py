from django.urls import path
from .views import cadastrar_noticias,index

urlpatterns = [
    path('',index,name='index'),
    path('noticias/cadastro', cadastrar_noticias, name='gerencia_noticia_listagem'),
]