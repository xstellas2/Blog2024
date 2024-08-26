from django.shortcuts import render
from .models import Noticia

# Create your views here.
def lista_noticia(request):
    noticias = Noticia.objects.all()
    contexto={
        'noticias': noticias
    }
    return render(request, 'noticia/lista_noticias.html',contexto)

