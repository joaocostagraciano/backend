from django.db import models

class pessoa(models.Model):
    nome = models.CharField(max_length=50)
