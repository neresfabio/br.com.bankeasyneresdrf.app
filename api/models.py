from django.db import models

# Crie seus modelos aqui.

class Cliente(models.Model):
    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)  # Telefone opcional
    data_nascimento = models.DateField()
    data_criacao = models.DateTimeField(auto_now_add=True)  # Registro criado automaticamente
    created_at = models.DateTimeField(auto_now_add=True)    # Timestamp para criação
    updated_at = models.DateTimeField(auto_now=True)        # Timestamp para atualização

    def __str__(self):
        return f"{self.nome_completo} ({self.cpf})"