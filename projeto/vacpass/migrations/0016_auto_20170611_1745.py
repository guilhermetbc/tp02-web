# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-11 17:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacpass', '0015_auto_20170610_0159'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitacao',
            name='recomendacao',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='controlevencimento',
            name='dose',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacpass.DoseVacina'),
        ),
        migrations.AlterField(
            model_name='solicitacao',
            name='status',
            field=models.IntegerField(choices=[(1, 'Pendente'), (2, 'Resolvido'), (3, 'Negada')], default=1),
        ),
    ]
