from django.shortcuts import render, redirect
from .models import Noticia
from .forms import NoticiaForm

# Create your views here.
def lista_noticia(request):
    noticias = Noticia.objects.all()
    contexto={
        'noticias': noticias
    }
    return render(request, 'noticia/lista_noticias.html',contexto)

def pre_cadastro_noticia(request):
    
    if request.method == 'POST':
        print(request.POST)
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('noticias') # procura uma rota com name 'noticias'
    else:
        form = NoticiaForm()

    contexto = {
        'form': form
    }
    return render(request, 'noticia/cadastro_noticia.html',contexto)

