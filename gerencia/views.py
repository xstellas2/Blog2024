from django.shortcuts import render,redirect
from noticia.models import Noticia
from noticia.forms import NoticiaForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Create your views here.
@login_required
def inicio_gerencia(request):
    return render(request, 'gerencia/inicio.html')

def listagem_noticia(request):
    noticias = Noticia.objects.all()
    contexto = {
        'noticias': noticias
    }
    return render(request, 'gerencia/listagem_noticia.html',contexto)


def cadastro_noticia(request):
    
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save() 
            return redirect('gerencia:listagem_noticia')
    else: 
        form = NoticiaForm()
    
    contexto = {
        'form': form
    }
    return render(request, 'gerencia/cadastro_noticia.html',contexto)

@login_required
def editar_noticia(request, id):
    noticia = Noticia.objects.get(id=id)
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('gerencia:listagem_noticia')
    else:
        form = NoticiaForm(instance=noticia)
    
    contexto = {
        'form': form
    }
    return render(request, 'gerencia/cadastro_noticia.html',contexto)