from django import forms
from esiomotores.core.models import CustomerMKT


class CustomerMKTForm(forms.ModelForm):
    email = forms.CharField(error_messages={'invalid': 'ERRO: Informe um endereço de email válido.'})

    class Meta:
        model = CustomerMKT
        fields = ['name', 'email']

    def clean_name(self):
        name = self.cleaned_data['name']
        words = [w.capitalize() for w in name.split()]
        return " ".join(words)

    def clean_email(self):
        email = self.cleaned_data['email']
        words = [w.lower() for w in email.split()]
        return " ".join(words)
