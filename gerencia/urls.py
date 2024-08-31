from django.urls import path
from .views import inicio_gerencia, listagem_noticia,cadastro_noticia

app_name = 'gerencia'
urlpatterns = [
    path('', inicio_gerencia, name='index'),
    path('noticias/', listagem_noticia, name='listagem_noticia'),
    path('noticias/cadastro', cadastro_noticia, name='cadastro_noticia'),
    # Add your URL patterns here
]