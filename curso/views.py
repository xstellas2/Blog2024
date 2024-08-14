from django.shortcuts import render
from .models import Modalidade, Curso, Aluno

# Create your views here.
def index(request):
    cursos = Curso.objects.all() # Select do django
    contexto = {
        'lista': cursos,
    }
    return render(request, 'curso/index.html',contexto)


def details(request, curso_id):
    c = Curso.objects.get(id=curso_id)
    alunos = Aluno.objects.filter(curso=c)
    contexto = {
        'curso': c,
        'alunos' : alunos
    }
    return render(request, 'curso/detalhe_curso.html',contexto)

def noticias(request):
    return render(request, 'curso/noticia.html')