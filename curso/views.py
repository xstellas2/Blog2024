from django.shortcuts import render
from .models import Modalidade, Curso, Aluno

# Create your views here.
def index(request):
    cursos = Curso.objects.all() # Select do django
    contexto = {
        'cursos': cursos,
    }
    return render(request, 'curso/index.html',contexto)