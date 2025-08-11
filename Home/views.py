from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from .models import Pacote, Cupom, MaisProcurado, Passeio, Promocao, Hospedagem, Evento, Profile
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
        # Cria o perfil associado ao usuário
        profile = Profile.objects.create(user=user, address=endereco)
        profile.save()
        return redirect('login')
    return render(request, 'home/cadastro.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user_obj = User.objects.get(username=username)
        except User.DoesNotExist:
            return render(request, 'home/login.html', {'erro': 'Conta não existe.'})

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            return render(request, 'home/login.html', {'erro': 'Usuário ou senha inválidos.'})
    return render(request, 'home/login.html')

def logout_view(request):
    logout(request)
    return redirect('inicio')

@login_required
def perfil(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'change_password':
            old_password = request.POST.get('old_password')
            new_password1 = request.POST.get('new_password1')
            new_password2 = request.POST.get('new_password2')

            if not request.user.check_password(old_password):
                return render(request, 'home/perfil.html', {'msg': 'Senha antiga incorreta.', 'user_profile': user_profile})
            if new_password1 != new_password2:
                return render(request, 'home/perfil.html', {'msg': 'As novas senhas não coincidem.', 'user_profile': user_profile})
            if len(new_password1) < 8: # Example: minimum password length
                return render(request, 'home/perfil.html', {'msg': 'A nova senha deve ter pelo menos 8 caracteres.', 'user_profile': user_profile})

            request.user.set_password(new_password1)
            request.user.save()
            update_session_auth_hash(request, request.user)  # Important: keep the user logged in
            return render(request, 'home/perfil.html', {'msg': 'Senha alterada com sucesso!', 'user_profile': user_profile})
        elif action == 'update_profile_picture':
            if 'profile_picture' in request.FILES:
                user_profile.profile_picture = request.FILES['profile_picture']
                user_profile.save()
                return render(request, 'home/perfil.html', {'msg': 'Foto de perfil atualizada com sucesso!', 'user_profile': user_profile})
            else:
                return render(request, 'home/perfil.html', {'msg': 'Nenhuma imagem selecionada.', 'user_profile': user_profile})
        else: # Default action: update profile data
            request.user.first_name = request.POST.get('nome', request.user.first_name)
            request.user.email = request.POST.get('email', request.user.email)
            request.user.save()

            user_profile.address = request.POST.get('endereco', user_profile.address)
            user_profile.save()

            return render(request, 'home/perfil.html', {'msg': 'Dados atualizados com sucesso!', 'user_profile': user_profile})

    return render(request, 'home/perfil.html', {'user_profile': user_profile})

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

def politica_privacidade(request):
    return render(request, 'home/politica_privacidade.html')

def termos_servico(request):
    return render(request, 'home/termos_servico.html')
