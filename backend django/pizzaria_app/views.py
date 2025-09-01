from django.shortcuts import render, redirect
from .forms import ClienteForm, AdminForm

def home(request):
    return render(request, 'pizzaria-app/home.html')  # Template com hífen, correspondente à pasta

def cadastro_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClienteForm()
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