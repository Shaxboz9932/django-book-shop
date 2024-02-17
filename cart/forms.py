from django import forms


class CartAddForm(forms.Form):
    quantity = forms.CharField(
        label='Quantity',
        widget=forms.NumberInput(attrs={
            'class': 'form-control mt-2',
            'min': 1
    }))

