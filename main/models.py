from django.db import models
from django.contrib.auth.models import User

class Categorias(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.nome)
    
class Receitas(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=16, decimal_places=2)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    data = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Despesas(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=16, decimal_places=2)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    data = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)