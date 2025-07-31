from django.contrib import admin
from .models import Pacote
from .models import Cupom
from .models import MaisProcurado

admin.site.register(Pacote)
admin.site.register(Cupom)
admin.site.register(MaisProcurado)