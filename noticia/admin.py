from django.contrib import admin
from .models import Noticia

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao', 'autor')
    search_fields = ('titulo', 'autor')
    date_hierarchy = 'data_publicacao'
    ordering = ('-data_publicacao',)

