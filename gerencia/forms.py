from django import forms
from .models import Noticia

class NoticiaForm(forms.ModelForm):
    
    class Meta:
        model = Noticia
        fields = '__all__'
        widgets = {
            'data_publicacao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), 
            'texto': forms.Textarea(attrs={'class': 'form-control'}),  
            'titulo': forms.TextInput(attrs={'class': 'form-control'}), 
            'image': forms.FileInput(attrs={'class': 'form-control'}), 
            'categoria': forms.Select(attrs={'class': 'form-control'}),

        }
