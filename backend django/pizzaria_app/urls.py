from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/customer/', views.cliente_opcoes, name='cliente_opcoes'),
    path('cadastro/customer/cadastrar/', views.cadastro_cliente, name='cadastro_cliente'),
    path('cadastro/admin/', views.cadastro_admin, name='cadastro_admin'),
    path('cadastro/customer/entrar/', views.login_customer, name='login_customer'),
]