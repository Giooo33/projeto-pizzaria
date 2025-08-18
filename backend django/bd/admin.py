from django.contrib import admin
from .models import Pizza, Drink, Admin, Tamanhos, Volumes

class TamanhosAdmin(admin.ModelAdmin):
    list_display = ('id', 'tamanhos_nome',)
    search_fields = ('tamanhos_nome',)
    list_filter = ('tamanhos_nome',)

class VolumesAdmin(admin.ModelAdmin):
    list_display = ('id', 'volumes_nome',)
    search_fields = ('volumes_nome',)
    list_filter = ('volumes_nome',)

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'ingredients')

class DrinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

class AdminAdmin(admin.ModelAdmin):

    list_display = ('name', 'telephone')
    search_fields = ('name', 'telephone')
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Tamanhos, TamanhosAdmin)
admin.site.register(Volumes, VolumesAdmin)
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Drink, DrinkAdmin)
admin.site.register(Admin, AdminAdmin)


# Register your models here.
