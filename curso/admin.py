from django.contrib import admin
from .models import Modalidade, Curso, Aluno
# Register your models here.

@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'modalidade', 'vagas', 'inscritos']

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone', 'data_nascimento', 'curso']    
    