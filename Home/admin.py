from django.contrib import admin
from .models import Pacote, Cupom, MaisProcurado, Passeio, PasseioImage, Hospedagem, HospedagemImage, Evento, EventoImage

class PasseioImageInline(admin.TabularInline):
    model = PasseioImage
    extra = 1

class PasseioAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    inlines = [PasseioImageInline]
    fieldsets = (
        (None, {
            'fields': ('nome', 'imagem', 'descricao', 'localizacao', 'telefone', 'valores', 'horarios', 'redes_sociais', 'mapa_link')
        }),
    )

class HospedagemImageInline(admin.TabularInline):
    model = HospedagemImage
    extra = 1

class HospedagemAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    inlines = [HospedagemImageInline]
    fieldsets = (
        (None, {
            'fields': ('nome', 'imagem', 'descricao', 'localizacao', 'telefone', 'valores', 'horarios', 'redes_sociais', 'mapa_link')
        }),
    )

class EventoImageInline(admin.TabularInline):
    model = EventoImage
    extra = 1

class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    inlines = [EventoImageInline]
    fieldsets = (
        (None, {
            'fields': ('nome', 'imagem', 'descricao', 'localizacao', 'telefone', 'valores', 'horarios', 'redes_sociais', 'mapa_link')
        }),
    )

admin.site.register(Pacote)
admin.site.register(Cupom)
admin.site.register(MaisProcurado)
admin.site.register(Passeio, PasseioAdmin)
admin.site.register(Hospedagem, HospedagemAdmin)
admin.site.register(Evento, EventoAdmin)
