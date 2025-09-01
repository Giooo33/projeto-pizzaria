from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from models import Customer

class CustomerForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput, label="Senha")
    confirmar_senha = forms.CharField(widget=forms.PasswordInput, label="Confirmar Senha")

    class Meta:
        model = Customer
        fields = ['nome', 'email', 'telefone']

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')
        confirmar_senha = cleaned_data.get('confirmar_senha')
        if senha and confirmar_senha and senha != confirmar_senha:
            raise forms.ValidationError("As senhas não coincidem.")
        return cleaned_data

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['email'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['senha']
        )
        customer = super().save(commit=False)
        customer.user = user
        if commit:
            customer.save()
        return customer

class AdminForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, label="E-mail ou Usuário")
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")