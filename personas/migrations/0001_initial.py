# Generated by Django 3.0.4 on 2020-03-22 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('sobrenome', models.CharField(blank=True, max_length=200, null=True, verbose_name='Sobrenome')),
                ('cpf', models.IntegerField(verbose_name='CPF/CNPJ')),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outros')], max_length=1, verbose_name='Gênero')),
                ('dtNascimento', models.DateField(verbose_name='Data de nascimento')),
                ('pontos', models.IntegerField(blank=True, default=0, null=True, verbose_name='Pontos')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=' Criado em ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name=' Atualizado em ')),
            ],
            options={
                'verbose_name': 'Prestador',
                'verbose_name_plural': 'Prestadores',
            },
        ),
        migrations.CreateModel(
            name='Prestador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome/Razão')),
                ('sobreNome', models.CharField(blank=True, max_length=200, null=True, verbose_name='Sobrenome')),
                ('cpfCnpj', models.IntegerField(verbose_name='CPF/CNPJ')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('usuario', models.CharField(max_length=12, verbose_name='Usuário')),
                ('senha', models.CharField(max_length=20, verbose_name='Senha')),
                ('qrCode', models.ImageField(blank=True, null=True, upload_to='', verbose_name='QrCode')),
                ('perfil', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto Perfil')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=' Criado em ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name=' Atualizado em ')),
            ],
            options={
                'verbose_name': 'Prestador',
                'verbose_name_plural': 'Prestadores',
            },
        ),
    ]