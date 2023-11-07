from django.db import models
from django.utils import timezone


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

class ModeloExpiravel(models.Model):
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)


class SeuModelo(models.Model):
    # Defina os campos do seu modelo
    campo1 = models.CharField(max_length=100)
    campo2 = models.IntegerField()
    data_de_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.campo1  # Esta é uma representação de texto do modelo para facilitar a identificação

    #
    
    """
    @staticmethod
    def excluir_apos_24_horas():
        agora = timezone.now()
        modelos_a_excluir = SeuModelo.objects.filter(data_de_criacao__lt=agora - timezone.timedelta(hours=24))
        modelos_a_excluir.delete()
    """
