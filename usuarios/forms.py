from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserBlog

class UserBlogCreationForm(UserCreationForm):
    cpf = forms.CharField(max_length=11, required=True, help_text="Digite seu CPF sem pontos ou traços.")
    nome_cidade = forms.CharField(max_length=100, required=False)
    nome_mae = forms.CharField(max_length=100, required=False)
    endereco = forms.CharField(max_length=255, required=False)
    nome_bairro = forms.CharField(max_length=100, required=False)

    class Meta:
        model = UserBlog
        fields = ('username', 'cpf', 'email', 'password1', 'password2', 'nome_cidade', 'nome_mae', 'endereco', 'nome_bairro')
