from django.db import models

# Create your models here.

class Estado(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.nome} ({self.sigla})"

class Cidade(models.Model):
     nome = models.CharField(max_length=50)
     Estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

     def __str__(self):
        return f"{self.nome} ({self.Estado.sigla})"

class pessoa(models.Model):
    nome = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    data_nascimento = models.DateField(max_length=50)
    telefone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return f"{self.nome} ({self.data_nascimento})"    