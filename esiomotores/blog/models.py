from django.db import models
from django.shortcuts import resolve_url as r
from s3direct.fields import S3DirectField


class Blogs(models.Model):
    BLOG_DIR = '/noticias/'

    CATALOG = 'catalogos'
    EVENT = 'eventos'
    NEWS = 'novidades'
    PROMO = 'promocoes'
    OTHER = 'outros'

    KINDS = ((CATALOG, 'CATÁLOGOS'),
             (EVENT, 'EVENTOS'),
             (NEWS, 'NOVIDADES'),
             (PROMO, 'PROMOÇÕES'),
             (OTHER, 'OUTROS'))

    title = models.CharField('TÍTULO', max_length=50)
    slug = models.SlugField('SLUG', max_length=50, primary_key=True)
    category = models.CharField('CATEGORIA', max_length=15, choices=KINDS)
    publish = models.BooleanField('PUBLICAR?', default=False)
    created_at = models.DateTimeField('CRIADO EM', auto_now_add=True)

    class Meta:
        unique_together = (('slug', 'created_at'),)
        verbose_name = 'CADASTRO DE NOTÍCIA'
        verbose_name_plural = 'CADASTRO DE NOTÍCIAS'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return r('one_blog', slug=self.slug)


class Contents(models.Model):
    title = models.ForeignKey('Blogs', verbose_name='NOME')
    order_out = models.IntegerField('ORDEM DE POSTAGEM')
    text = models.TextField('TEXTO', max_length=700, blank=True)
    picture = S3DirectField(verbose_name='IMAGEM', dest='AmazonS3', blank=True)
    inverse = models.BooleanField('INVERTER ORDEM?', default=False)

    class Meta:
        unique_together = (('title', 'order_out'),)
        verbose_name = 'CONTEÚDO DE NOTÍCIA'
        verbose_name_plural = 'CONTEÚDOS DE NOTÍCIA'
        ordering = ('order_out',)

    def __str__(self):
        return str(self.order_out)
