from django import forms
from .models import Employee


class FirstTimeEmployeeForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Employee
        fields = [
            "name",
            "assigned_zip_code",
        ]
