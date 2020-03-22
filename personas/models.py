from django.db import models

class Prestador(models.Model):
    nome = models.CharField('Nome/Razão', max_length=200)
    sobreNome = models.CharField('Sobrenome', max_length=200, null=True, blank=True)
    cpfCnpj = models.IntegerField('CPF/CNPJ')
    email = models.EmailField('E-mail')
    usuario = models.CharField('Usuário', max_length=12)
    senha = models.CharField('Senha', max_length=20)
    qrCode = models.ImageField('QrCode', blank=True, null=True)
    perfil = models.ImageField('Foto Perfil', blank=True, null=True)
    created_at = models.DateTimeField(' Criado em ', auto_now_add=True)         # Grava data de criação
    updated_at = models.DateTimeField(' Atualizado em ', auto_now=True)          # Grava data de atualização

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Prestador'
        verbose_name_plural = 'Prestadores'

class Cliente(models.Model):
    M = 'M'
    F = 'F'
    O = 'O'
    GENEROS = [(M, 'Masculino'), (F, 'Feminino'), (O, 'Outros')]

    nome = models.CharField('Nome', max_length=200)
    sobrenome = models.CharField('Sobrenome', max_length=200, null=True, blank=True)
    cpf = models.IntegerField('CPF/CNPJ')
    genero = models.CharField('Gênero', max_length=1, choices=GENEROS)
    dtNascimento = models.DateField('Data de nascimento')
    pontos = models.IntegerField('Pontos', default=0, blank=True, null=True)
    created_at = models.DateTimeField(' Criado em ', auto_now_add=True)         # Grava data de criação
    updated_at = models.DateTimeField(' Atualizado em ', auto_now=True)          # Grava data de atualização

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Prestador'
        verbose_name_plural = 'Prestadores'
