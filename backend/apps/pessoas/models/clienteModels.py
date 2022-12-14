from django.conf import settings
from django.db import models

class ClienteModel(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, related_name='user_client')
    nome = models.CharField(max_length=224)
    cpf = models.CharField(max_length=11)
    email = models.EmailField(max_length=224)
    telefone1 = models.CharField(max_length=12)
    telefone2 = models.CharField(null=True, max_length=12)
    logradouro = models.CharField(null=True, max_length=224)
    numero = models.CharField(null=True, max_length=20)
    complemento = models.CharField(null=True, max_length=224)
    bairro = models.CharField(null=True, max_length=224)
    cidade = models.CharField(null=True, max_length=224)
    estado = models.CharField(null=True, max_length=224)
    pais = models.CharField(null=True, max_length=224)
    cep = models.CharField(null=True, max_length=8)

    def __str__(self):
        return f"Client: {self.nome}"