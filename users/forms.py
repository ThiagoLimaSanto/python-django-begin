# from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']
#         label = {'username': 'login', 'password': 'senha'}

class LoginForm(forms.Form):
    login = forms.CharField(max_length=30)
    senha = forms.CharField(max_length=30, widget=forms.PasswordInput())
    
    def clean_login(self):
        nome = self.cleaned_data['login']
        
        if not(nome.isalnum()):
            raise ValidationError('O nome do usuario nao pode ter caracteres especiais!')
        
        return nome