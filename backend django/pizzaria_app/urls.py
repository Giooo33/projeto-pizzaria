from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial (home.html)
    path('cadastro/cliente/', views.cadastro_cliente, name='cadastro_cliente'),  # Cadastro de cliente
    path('cadastro/admin/', views.cadastro_admin, name='cadastro_admin'),  # Cadastro de admin
]