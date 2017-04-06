# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 19:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import s3direct.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('title', models.CharField(max_length=50, verbose_name='TÍTULO')),
                ('slug', models.SlugField(primary_key=True, serialize=False, verbose_name='SLUG')),
                ('category', models.CharField(choices=[('catalogos', 'CATÁLOGOS'), ('eventos', 'EVENTOS'), ('novidades', 'NOVIDADES'), ('promocoes', 'PROMOÇÕES'), ('outros', 'OUTROS')], max_length=15, verbose_name='CATEGORIA')),
                ('publish', models.BooleanField(default=False, verbose_name='PUBLICAR?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='CRIADO EM')),
            ],
            options={
                'verbose_name': 'CADASTRO DE NOTÍCIA',
                'verbose_name_plural': 'CADASTRO DE NOTÍCIAS',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Contents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_out', models.IntegerField(verbose_name='ORDEM DE POSTAGEM')),
                ('text', models.TextField(blank=True, max_length=700, verbose_name='TEXTO')),
                ('picture', s3direct.fields.S3DirectField(blank=True, verbose_name='IMAGEM')),
                ('inverse', models.BooleanField(default=False, verbose_name='INVERTER ORDEM?')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blogs', verbose_name='NOME')),
            ],
            options={
                'verbose_name': 'CONTEÚDO DE NOTÍCIA',
                'verbose_name_plural': 'CONTEÚDOS DE NOTÍCIA',
                'ordering': ('order_out',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='blogs',
            unique_together=set([('slug', 'created_at')]),
        ),
        migrations.AlterUniqueTogether(
            name='contents',
            unique_together=set([('title', 'order_out')]),
        ),
    ]