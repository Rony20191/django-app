from django.db import models


class Usuario(models.Model):
    #unique=True
    nome=models.CharField(max_length=80)
    sobrenome=models.CharField(max_length=20)
    senha=models.CharField(max_length=8)

