from django.db import models

class Pacote(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='pacotes/')
    cafe_da_manha = models.BooleanField(default=False)
    translados = models.BooleanField(default=False)
    hospedagem = models.BooleanField(default=False)
    viagem = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Cupom(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    codigo = models.CharField(max_length=30)
    validade = models.DateField()

    def __str__(self):
        return self.titulo

class MaisProcurado(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='mais_procurados/')
    descricao1 = models.CharField(max_length=100, blank=True)
    descricao2 = models.CharField(max_length=100, blank=True)
    descricao3 = models.CharField(max_length=100, blank=True)
    descricao4 = models.CharField(max_length=100, blank=True)
    botao_texto = models.CharField(max_length=50, default="VER MAIS!")
    botao_link = models.URLField(blank=True)

    def __str__(self):
        return self.titulo

class Passeio(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='passeios/')
    descricao = models.TextField(default='')
    localizacao = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    valores = models.CharField(max_length=100, blank=True)
    horarios = models.CharField(max_length=100, blank=True)
    redes_sociais = models.URLField(blank=True)
    mapa_link = models.URLField(max_length=500, blank=True, help_text="Cole o link do Google Maps aqui")

    def __str__(self):
        return self.nome

class PasseioImage(models.Model):
    passeio = models.ForeignKey(Passeio, related_name='imagens', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='passeios/galeria/')

    def __str__(self):
        return f"Imagem de {self.passeio.nome}"

class Promocao(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='promocoes/')

    def __str__(self):
        return self.titulo

class Hospedagem(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='hospedagens/')
    descricao = models.TextField(default='')
    localizacao = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    valores = models.CharField(max_length=100, blank=True)
    horarios = models.CharField(max_length=100, blank=True)
    redes_sociais = models.URLField(blank=True)
    mapa_link = models.URLField(max_length=500, blank=True, help_text="Cole o link do Google Maps aqui")

    def __str__(self):
        return self.nome

class HospedagemImage(models.Model):
    hospedagem = models.ForeignKey(Hospedagem, related_name='imagens', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='hospedagens/galeria/')

    def __str__(self):
        return f"Imagem de {self.hospedagem.nome}"

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='eventos/')
    descricao = models.TextField(default='')
    localizacao = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    valores = models.CharField(max_length=100, blank=True)
    horarios = models.CharField(max_length=100, blank=True)
    redes_sociais = models.URLField(blank=True)
    mapa_link = models.URLField(max_length=500, blank=True, help_text="Cole o link do Google Maps aqui")

    def __str__(self):
        return self.nome

class EventoImage(models.Model):
    evento = models.ForeignKey(Evento, related_name='imagens', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='eventos/galeria/')

    def __str__(self):
        return f"Imagem de {self.evento.nome}"