# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerMKT',
            fields=[
                ('name', models.CharField(max_length=50, verbose_name='NOME')),
                ('email', models.EmailField(max_length=60, primary_key=True, serialize=False, verbose_name='EMAIL')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='CRIADO EM')),
            ],
            options={
                'verbose_name': 'CLIENTE MARKETING',
                'verbose_name_plural': 'CLIENTES MARKETING',
                'ordering': ('-created_at',),
            },
        ),
    ]
