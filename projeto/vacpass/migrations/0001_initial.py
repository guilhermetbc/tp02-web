# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-12-06 12:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cartao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='ControleVencimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('avisado', models.BooleanField(default=False)),
                ('cartao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacpass.Cartao')),
            ],
        ),
        migrations.CreateModel(
            name='Dependente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.IntegerField(choices=[(1, 'CPF'), (2, 'RG'), (3, 'certidao')])),
                ('nome', models.CharField(max_length=50)),
                ('ndocumento', models.CharField(max_length=50)),
                ('cartao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacpass.Cartao')),
            ],
        ),
        migrations.CreateModel(
            name='DoseVacina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dose', models.IntegerField()),
                ('idade', models.CharField(max_length=50)),
                ('duracao_meses', models.IntegerField()),
                ('cartao', models.ManyToManyField(through='vacpass.ControleVencimento', to='vacpass.Cartao')),
            ],
        ),
        migrations.CreateModel(
            name='Solicitacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('datahora', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(1, 'Pendente'), (2, 'Resolvido'), (3, 'Negada')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nascimento', models.DateField()),
                ('cartao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacpass.Cartao')),
                ('django_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vacina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('funcionalidade', models.CharField(default='', max_length=500)),
                ('publico_alvo', models.CharField(default='', max_length=500)),
                ('disponibilidade', models.CharField(default='', max_length=500)),
                ('proibitivos', models.CharField(default='', max_length=500)),
                ('preco', models.FloatField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='solicitacao',
            name='solicitante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacpass.Usuario'),
        ),
        migrations.AddField(
            model_name='solicitacao',
            name='vacina',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vacpass.Vacina', to_field='nome'),
        ),
        migrations.AddField(
            model_name='dosevacina',
            name='vacina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacpass.Vacina'),
        ),
        migrations.AddField(
            model_name='dependente',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacpass.Usuario'),
        ),
        migrations.AddField(
            model_name='controlevencimento',
            name='dose',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacpass.DoseVacina'),
        ),
    ]