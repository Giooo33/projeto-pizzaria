from django.contrib import admin
from .models import Pizza, Drink, Admin, Customer

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'ingredients')

class DrinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

class AdminAdmin(admin.ModelAdmin):
    list_display = ('name', 'telephone')
    search_fields = ('name', 'telephone')

admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Drink, DrinkAdmin)
admin.site.register(Admin, AdminAdmin)


# Register your models here.
