from django.core.exceptions import ValidationError


def validate_phone(value):
    if not value.isdigit():
        raise ValidationError('Este campo deve conter apenas números', 'digit')
    elif value[2]=='9' and len(value)!=11:
        raise ValidationError('Telefones celulares devem ter 11 dígitos', 'mobile_length')
    elif value[2]!='9' and len(value)!=10:
        raise ValidationError('Telefones fixos deves ter 10 dígitos', 'fixed_length')