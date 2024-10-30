from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserBlogCreationForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Autenticar o usuário
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # Loga o usuário
            return redirect('gerencia:gerencia_inicial')  # Redireciona após login
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'usuarios/login.html')

def logout_view(request):
    logout(request) 
    return redirect('usuarios:login')  



def register(request):
    if request.method == 'POST':
        form = UserBlogCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso! Você já pode fazer login.')
            return redirect('usuarios:login')  
    else:
        form = UserBlogCreationForm()

    return render(request, 'usuarios/register.html', {'form': form})
