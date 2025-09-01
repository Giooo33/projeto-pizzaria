from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ClienteForm(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    senha = forms.CharField(widget=forms.PasswordInput)
    confirmar_senha = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')
        confirmar_senha = cleaned_data.get('confirmar_senha')
        if senha and confirmar_senha and senha != confirmar_senha:
            raise forms.ValidationError("As senhas não coincidem.")
        return cleaned_data

class AdminForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']