from django.urls import path
from .views import inicio_gerencia, listagem_noticia, cadastro_noticia, edicao_noticia, listagem_categorias, criar_categoria, edicao_categoria, deletar_categoria

app_name = 'gerencia'

urlpatterns = [
    path('', inicio_gerencia, name='gerencia_inicial'),
    path('noticias/', listagem_noticia, name='listagem_noticia'),
    path('noticias/cadastro', cadastro_noticia, name='cadastro_noticia'),
    path('noticias/edicao_noticia/<int:id>', edicao_noticia, name='edicao_noticia'),
    path('categorias/', listagem_categorias, name='listagem_categorias'),
    path('categorias/criar/', criar_categoria, name='criar_categoria'),
    path('categorias/edicao_noticia/<int:id>/', edicao_categoria, name='edicao_categoria'),
    path('categorias/deletar/<int:id>/', deletar_categoria, name='deletar_categoria'),
]