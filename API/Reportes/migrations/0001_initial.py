# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-08 18:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Centros', '0001_initial'),
        ('Elementos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ElementosReporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('elemento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Elementos.Elemento')),
            ],
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora_ing', models.DateTimeField(auto_now_add=True)),
                ('fecha_hora_sal', models.DateTimeField(blank=True, null=True)),
                ('pro_rep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sede_rep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Centros.Sede')),
            ],
        ),
        migrations.AddField(
            model_name='elementosreporte',
            name='reporte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reportes.Reporte'),
        ),
        migrations.AlterUniqueTogether(
            name='reporte',
            unique_together=set([('fecha_hora_ing', 'pro_rep')]),
        ),
    ]