from django.contrib import admin

from api.models import Cliente

# Register your models here.

admin.site.register(Cliente)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cpf', 'email', 'data_criacao')
    search_fields = ('nome_completo', 'cpf', 'email')