from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomerForm, AdminForm, LoginForm

def home(request):
    return render(request, 'pizzaria-app/home.html')

def cliente_opcoes(request):
    return render(request, 'pizzaria-app/cliente_opcoes.html')

def cadastro_cliente(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomerForm()
    return render(request, 'pizzaria-app/cadastro_cliente.html', {'form': form})

def cadastro_admin(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_staff = True
            user.save()
            return redirect('home')
    else:
        form = AdminForm()
    return render(request, 'pizzaria-app/cadastro_admin.html', {'form': form})

def login_customer(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Usuário ou senha inválidos.")
    else:
        form = LoginForm()
    return render(request, 'pizzaria-app/login_customer.html', {'form': form})