from django.db import models


class CustomerMKT(models.Model):
    name = models.CharField('NOME', max_length=50)
    email = models.EmailField('EMAIL', max_length=60, primary_key=True,
                              error_messages={'unique': 'ERRO: Este e-mail já está cadastrado.'})
    created_at = models.DateTimeField('CRIADO EM', auto_now_add=True)

    class Meta():
        verbose_name_plural = 'CLIENTES MARKETING'
        verbose_name = 'CLIENTE MARKETING'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
