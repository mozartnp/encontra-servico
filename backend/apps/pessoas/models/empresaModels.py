from django.conf import settings
from django.db import models

class EmpresaModel(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, related_name='user_company')
    nome_fantasia = models.CharField(max_length=224)
    razao_social = models.CharField(null=True, max_length=224)
    cnpj = models.CharField(max_length=15)
    ie = models.CharField(null=True, max_length=20)
    email = models.EmailField(max_length=224)
    telefone1 = models.CharField(max_length=12)
    telefone2 = models.CharField(null=True, max_length=12)
    logradouro = models.CharField(null=True, max_length=224)
    numero = models.CharField(null=True, max_length=20)
    bairro = models.CharField(null=True, max_length=224)
    cidade = models.CharField(null=True, max_length=224)
    estado = models.CharField(null=True, max_length=224)
    pais = models.CharField(null=True, max_length=224)
    complemento = models.CharField(null=True, max_length=224)
    cep = models.CharField(null=True, max_length=8)
    categoria = models.CharField(max_length=224)

    def __str__(self):
        return f"Company: {self.nome_fantasia}"