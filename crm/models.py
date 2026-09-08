from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class Lead(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Lead de {self.cliente}"

class Interacao(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    descricao = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Interacao em {self.lead}"
