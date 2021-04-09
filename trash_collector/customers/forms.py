from django import forms

from .models import Customer


# create a ModelForm
class CustomerForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Customer
        fields = [
            "name",
        ]

    def save(self, commit=True):
        # Overriding the save method to add user to auth group of Employee or Customer depending on if box is checked
        user = super(CustomerForm, self).save(commit=False)

        if commit:
            user.save()
            # if user.is_employee:
            #     employees = Group.objects.get(name="Employees")
            #     employees.user_set.add(user)
            # else:
            #     customers = Group.objects.get(name="Customers")
            #     customers.user_set.add(user)
        return user

