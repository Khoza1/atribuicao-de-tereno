from django.contrib import admin
from .models import Terreno,Documento,RecursoNatural

class TerrenoAdmin(admin.ModelAdmin):
    list_display = ('proprietario', 'uso_da_terra', 'localizacao', 'historico_transacoes')
    list_filter = ('uso_da_terra',)

admin.site.register(Terreno, TerrenoAdmin)
admin.site.register(Documento)
admin.site.register(RecursoNatural)
