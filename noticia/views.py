from django.shortcuts import render,redirect
from .models import Noticia
from .forms import NoticiaForm

# Create your views here.
def index(request):
    noticias = Noticia.objects.all()
    contexto={
        'noticias': noticias
    }
    return render(request, 'noticia/index.html',contexto)



