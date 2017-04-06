from django.apps import AppConfig

## Ao criarmos uma classe config, precisamos alterar no settings.py o INSTALLED_APPS,
## para que o mesmo passe a fazer referência a esta classe
## DE: 'esiomotores.contacts'
## PARA: 'esiomotores.contacts.apps.ContactConfig'
class ContactConfig(AppConfig):
    name = 'esiomotores.contacts'
    verbose_name = 'MENSAGENS RECEBIDAS DE USUÁRIOS'