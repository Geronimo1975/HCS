from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.userauths.models import User


class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John Doe'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'johndoe@gmail.com'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '*************'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '*************'}))

    class Meta:
        model = User
        fields = ['full_name', 'email', 'password1', 'password2', 'user_type']
        widgets = {
            'user_type': forms.Select(attrs={'class': 'form-select'})  # styling only!
        }

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'johndoe@gmail.com'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '*************'}))

    class Meta:
        model = User
        fields = ['email', 'password']