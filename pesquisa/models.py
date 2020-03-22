from django.db import models
from personas.models import Prestador

class Pergunta(models.Model):
    numero = models.IntegerField('Número')
    texto = models.CharField('Texto', max_length=300)
    classe = modesl.CharField('Classe', max_length=12)

class Questionario(models.Model):
    numero = models.ManyToManyField(Pergunta, through='Formulario', through_fields=('questionario', 'pergunta'))
    descricao = models.CharField(max_length=100)
    prestador = models.ForeignKey(Prestador, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Criado em ', auto_now_add=True)         # Grava data de criação
    updated_at = models.DateTimeField('Atualizado em ', auto_now=True)          # Grava data de atualização

class Formulario(models.Model):
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)

class Atendimento(models.Model):
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE)
    resposta = models.CharField(max_length=300, null=True, blank=True)
