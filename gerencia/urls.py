from django.urls import path
from .views import inicio_gerencia, listagem_noticia,cadastrar_noticia,editar_noticia, listar_categorias, criar_categoria, editar_categoria, deletar_categoria

app_name = 'gerencia'

urlpatterns = [
    path('', inicio_gerencia, name='gerencia_inicial'),
    path('noticias/', listagem_noticia, name='listagem_noticia'),
    path('noticias/cadastro', cadastrar_noticia, name='cadastro_noticia'),
    path('noticias/editar/<int:id>', editar_noticia, name='editar_noticia'),
    path('categorias/', listar_categorias, name='listar_categorias'),
    path('categorias/criar/', criar_categoria, name='criar_categoria'),
    path('categorias/editar/<int:id>/', editar_categoria, name='editar_categoria'),
    path('categorias/deletar/<int:id>/', deletar_categoria, name='deletar_categoria'),
]