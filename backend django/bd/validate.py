
#aqui eu vou criar um validator de senha para o admin
# se a senha for igual a "admin123" ela esta certa, se não estiver, ela vai retornar um erro e
#não vai deixar o admin ser criado 
# e o admin tera que colocar uma senha ate ser valida por 5 vezes 

from django.core.exceptions import ValidationError

def validate_password(password):
    if password != "admin123":
        raise ValidationError(
            ('%(password)s is not a valid password.'),
            params={'password': password},
        )
    return password

