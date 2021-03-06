# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-08 18:19
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
            name='Elemento',
            fields=[
                ('cod_ele', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('des_ele', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='TipoElemento',
            fields=[
                ('cod_tipo_ele', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('des_tipo_ele', models.CharField(max_length=45)),
            ],
        ),
        migrations.AddField(
            model_name='elemento',
            name='cod_tipoele_ele',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Elementos.TipoElemento'),
        ),
        migrations.AddField(
            model_name='elemento',
            name='pro_ele',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
