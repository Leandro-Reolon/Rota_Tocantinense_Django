from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Pacote
from django.contrib.auth.decorators import login_required

def inicio(request):
    pacotes = Pacote.objects.all()
    return render(request, 'home/inicio.html', {'pacotes': pacotes})

def cadastro(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        nome = request.POST['nome']
        endereco = request.POST['endereco']
        # Cria o usuário
        user = User.objects.create_user(username=username, email=email, password=password, first_name=nome)
        user.save()
        return redirect('login')
    return render(request, 'home/cadastro.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            return render(request, 'home/login.html', {'erro': 'Usuário ou senha inválidos'})
    return render(request, 'home/login.html')

def logout_view(request):
    logout(request)
    return redirect('inicio')

@login_required
def perfil(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST['nome']
        user.email = request.POST['email']
        user.save()
        return render(request, 'home/perfil.html', {'msg': 'Dados atualizados com sucesso!'})
    return render(request, 'home/perfil.html')