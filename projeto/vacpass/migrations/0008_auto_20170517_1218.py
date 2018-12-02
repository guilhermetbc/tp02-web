# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-17 12:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacpass', '0007_merge_20170425_0723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='controlevencimento',
            name='vacina',
        ),
        migrations.RemoveField(
            model_name='controlevencimento',
            name='vencimento',
        ),
        migrations.RemoveField(
            model_name='vacina',
            name='cartao',
        ),
        migrations.AddField(
            model_name='controlevencimento',
            name='dose',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='vacpass.DoseVacina'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dosevacina',
            name='cartao',
            field=models.ManyToManyField(through='vacpass.ControleVencimento', to='vacpass.Cartao'),
        ),
        migrations.AddField(
            model_name='dosevacina',
            name='duracao_meses',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
