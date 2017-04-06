from django.db import models
from esiomotores.contacts.validators import validate_phone


class Contact(models.Model):
    name = models.CharField('NOME', max_length=50)
    email = models.EmailField('EMAIL', max_length=60)
    phone = models.CharField('TELEFONE', max_length=11, validators=[validate_phone])
    msg = models.TextField('MENSAGEM', max_length=700)
    ipaddr = models.GenericIPAddressField('ENDEREÇO IP', null=True, blank=True)
    created_at = models.DateTimeField('ENVIADA EM', auto_now_add=True)

    class Meta():
        verbose_name_plural = 'MENSAGENS'
        verbose_name = 'MENSAGEM'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
