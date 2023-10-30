from django.db import models

class Terreno(models.Model):
    proprietario = models.CharField(max_length=100)
    limites_propriedade = models.TextField()
    uso_da_terra = models.CharField(max_length=100)
    historico_transacoes = models.TextField()
    localizacao = models.CharField(max_length=100)

    def __str__(self):
        return self.proprietario

class RecursoNatural(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.FloatField()
    tipo = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Documento(models.Model):
    terreno = models.ForeignKey(Terreno, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    arquivo = models.FileField(upload_to='documentos/')

    def __str__(self):
        return self.terreno
