from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome da pizza: ", null=True)
    ingredients = models.CharField(max_length=300, verbose_name="Descrição da pizza: ", null=True)
    size = models.CharField(max_length=50, verbose_name="Tamanho da pizza: ", null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Preço da pizza: ", null=True)
    
    def __str__(self):
        return self.name
    
class Drink(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome do drink: ", null=True)
    size = models.CharField(max_length=50, verbose_name="Tamanho do drink: ", null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Preço do drink: ", null=True)
    
    def __str__(self):
        return self.name

class Admin(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome do administrador: ", null=True)
    telephone = models.CharField(max_length=13, verbose_name="Telefone do administrador: ", null=True)
    cpf = models.CharField(max_length=14, verbose_name="CPF do administrador: ", null=True)
    password = models.CharField(max_length=100, verbose_name="Senha do administrador: ", null=True)

    def save(self, *args, **kwargs):
        if not self.password:
            self.password = "admin123"
        super().save(*args, **kwargs)

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

