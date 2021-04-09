from django import forms

from .models import Address


# create a ModelForm
class AddressForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Address
        fields = [
            "address1",
            "address2",
            "city_name",
            "state_code",
            "country_code",
            "zip_code"
        ]