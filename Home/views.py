from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Pacote, Cupom, MaisProcurado, Passeio, Promocao, Hospedagem, Evento
from django.contrib.auth.decorators import login_required

def inicio(request):
    pacotes = Pacote.objects.all()
    mais_procurados = MaisProcurado.objects.all()
    promocoes = Promocao.objects.all()
    return render(request, 'home/inicio.html', {
        'pacotes': pacotes,
        'mais_procurados': mais_procurados,
        'promocoes': promocoes
    })

def cadastro(request):
    if request.method == 'POST':
        if not request.POST.get('lgpd'):
            return render(request, 'home/cadastro.html', {'erro': 'Você deve aceitar os termos da LGPD.'})
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

def cupons(request):
    cupons = Cupom.objects.all()
    return render(request, 'home/cupons.html', {'cupons': cupons})

def sobrenos(request):
    return render(request, 'home/sobrenos.html')

def passeios(request):
    query = request.GET.get('q')
    if query:
        passeios = Passeio.objects.filter(nome__icontains=query)
    else:
        passeios = Passeio.objects.all()
    return render(request, 'home/passeios.html', {'passeios': passeios})

def passeio_detalhes(request, passeio_id):
    passeio = get_object_or_404(Passeio, pk=passeio_id)
    return render(request, 'home/passeio_detalhes.html', {'passeio': passeio})

def hospedagens(request):
    query = request.GET.get('q')
    if query:
        hospedagens = Hospedagem.objects.filter(nome__icontains=query)
    else:
        hospedagens = Hospedagem.objects.all()
    return render(request, 'home/hospedagens.html', {'hospedagens': hospedagens})

def hospedagem_detalhes(request, hospedagem_id):
    hospedagem = get_object_or_404(Hospedagem, pk=hospedagem_id)
    return render(request, 'home/hospedagem_detalhes.html', {'hospedagem': hospedagem})

def eventos(request):
    query = request.GET.get('q')
    if query:
        eventos = Evento.objects.filter(nome__icontains=query)
    else:
        eventos = Evento.objects.all()
    return render(request, 'home/eventos.html', {'eventos': eventos})

def evento_detalhes(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    return render(request, 'home/evento_detalhes.html', {'evento': evento})