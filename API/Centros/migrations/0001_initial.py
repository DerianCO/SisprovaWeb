# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-08 18:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Centro',
            fields=[
                ('cod_centro', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('nom_centro', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('cod_sede', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('nom_sede', models.CharField(max_length=45)),
                ('cod_centro_sede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Centros.Centro')),
            ],
        ),
    ]
