import re
from validate_docbr import CPF
from django.core.exceptions import ValidationError

def cpf_validate(value):
    cpf = CPF()
    if not cpf.validate(value):
        raise ValidationError(
            ("%(value)s is not a valid CPF"),
            params={"value": value},
    ) 

def telefone_validate(value):
    if not value.isdigit():
        raise ValidationError(
                ("%(value)s is not a valid phone number"),
                params={"value": value},
            )
    if len(value) != 11:
        raise ValidationError(
            ("%(value)s must be 11 digits"),
            params={"value": value},
        )
    return value