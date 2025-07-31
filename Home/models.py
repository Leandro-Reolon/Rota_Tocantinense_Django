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