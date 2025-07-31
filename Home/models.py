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