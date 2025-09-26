from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout 
from django.contrib.auth.forms import AuthenticationForm
from .forms import FormularioCadastroUsuario

def index(request):
    return render(request, 'index.html')

def cadastro_usuario(request):
    if request.method == 'POST':
        form = FormularioCadastroUsuario(request.POST)
        if form.is_valid():
            user = form.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, 'Cadastro realizado com sucesso!')
                return redirect('index')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = FormularioCadastroUsuario()
    
    return render(request, 'cadastro_usuario.html', {'form': form})

def logout_usuario(request):
    logout(request)
    messages.success(request, 'Você saiu do sistema com sucesso!')
    return redirect('index')