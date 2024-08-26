from django.shortcuts import render
from .models import Noticia
from .forms import NoticiaForm

# Create your views here.
def lista_noticia(request):
    noticias = Noticia.objects.all()
    contexto={
        'noticias': noticias
    }
    return render(request, 'noticia/lista_noticias.html',contexto)


def cadastrar_noticias(request):
    form = NoticiaForm()
    contexto={
        'form': form
    }
    return render(request, 'noticia/cadastrar_noticia.html',contexto)