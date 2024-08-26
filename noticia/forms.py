from django import forms
from .models import Noticia



class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'

        widgets = {
            'data_publicacao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),  # Usando DateInput para uma data
            'texto': forms.Textarea(attrs={'class': 'form-control'}),  # Correto
            'autor': forms.TextInput(attrs={'class': 'form-control'}),  # Correto
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),  # Correto
            'image': forms.FileInput(attrs={'class': 'form-control'}),  # Usando FileInput para um campo de arquivo
        }
