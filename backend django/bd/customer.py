from .models import Customer

class CustomerCustomer(Customer.ModelCustomer):

    list_display = ('name', 'telephone', 'cpf', 'address')
    search_fields = ('name', 'telephone', )
    list_display = ('name',)
    search_fields = ('name',)

Customer.site.register(Customer, CustomerCustomer)