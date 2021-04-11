from django import forms

from .models import Customer


# create a ModelForm
class CustomerForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Customer
        fields = [
            "name",
            "user",
            "dow",
            # "one_time_date",
            # "suspension_start_date",
            # "suspension_end_date",
            # "pickup_charge_amount",
            # "default_currency_code",
            "default_pickup_zipcode",
        ]


