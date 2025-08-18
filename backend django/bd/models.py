from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def validate_password(password):
    if password != "admin123":
        raise ValidationError(
            ('%(password)s não é uma senha válida.'),
            params={'password': password},
        )
    return True

class Tamanhos(models.Model):
    TAMANHOS_CHOICES = [
        ('Mini', '4 pedaços'),
        ('Pequena', '6 pedaços'),
        ('Média', '8 pedaços'),
        ('Grande', '10 pedaços'),
        ('Gigante', '12 pedaços'),
    ]

    tamanhos_nome = models.CharField(max_length=50, choices=TAMANHOS_CHOICES, verbose_name="Tamanho da pizza: ")

    def __str__(self):
        return self.tamanhos_nome
    
class Volumes(models.Model):
    VOLUME_CHOICES = [
        ('500ml', '500ml'),
        ('1L', '1L'),
        ('1.5L', '1.5L'),
        ('2L', '2L'),
    ]

    volumes_nome = models.CharField(max_length=50, choices=VOLUME_CHOICES, verbose_name="Volume do drink: ")

    def __str__(self):
        return self.volumes_nome

class Pizza(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome da pizza: ", null=True)
    ingredients = models.CharField(max_length=300, verbose_name="Descrição da pizza: ", null=True)
    class_choices = models.ForeignKey(Tamanhos, on_delete=models.CASCADE, verbose_name="Tamanho da pizza: ", blank=False, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Preço da pizza: ", null=True)
    
    def __str__(self):
        return self.name
    
class Drink(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome do drink: ", null=True)
    class_choices = models.ForeignKey(Volumes, on_delete=models.CASCADE, verbose_name="Volume do drink: ", blank=False, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Preço do drink: ", null=True)
    
    def __str__(self):
        return self.name

class Admin(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome do administrador: ", null=True)
    telephone = models.CharField(max_length=13, verbose_name="Telefone do administrador: ", null=True)
    cpf = models.CharField(max_length=14, verbose_name="CPF do administrador: ", null=True)
    password = models.CharField(max_length=100, validators=[validate_password], verbose_name="Senha de Admin: ", blank=True, null=True)
            
    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome do cliente: ", null=True)
    telephone = models.CharField(max_length=13, verbose_name="Telefone do cliente: ", null=True)
    cpf = models.CharField(max_length=14, verbose_name="CPF do cliente: ", null=True)
    password = models.CharField(max_length=100, verbose_name="Senha do cliente: ", null=True)
    address = models.CharField(max_length=100, verbose_name="Endereço do cliente", null= True)

    def __str__(self):
        return self.name

