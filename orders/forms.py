from django import forms

from orders.models import Order


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.IntegerField(label='Phone Number', help_text='Masalan: 931234567', widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 100000000, 'max': 999999999}))
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(label='City', widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city']

