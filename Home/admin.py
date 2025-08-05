from django.contrib import admin
from .models import Pacote, Cupom, MaisProcurado, Passeio, Promocao

admin.site.register(Pacote)
admin.site.register(Cupom)
admin.site.register(MaisProcurado)
admin.site.register(Passeio)
admin.site.register(Promocao)