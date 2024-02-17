from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'autofocus': 'off'}))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'off'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'autofocus': 'off'}))
    password2 = forms.CharField(label='Password Confirm', widget=forms.PasswordInput(attrs={'class': 'form-control', 'autofocus': 'off'}))

    class Meta:
        model =User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop('autofocus')
        self.fields['email'].widget.attrs.pop('autofocus')
        self.fields['password1'].widget.attrs.pop('autofocus')
        self.fields['password2'].widget.attrs.pop('autofocus')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
