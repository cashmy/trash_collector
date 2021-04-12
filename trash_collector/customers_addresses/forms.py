from django import forms

from .models import CustomerAddress


# create a ModelForm
class CustomerAddressForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = CustomerAddress
        fields = [
            ''
        ]