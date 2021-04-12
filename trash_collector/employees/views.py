from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from .models import Employee
from django.urls import reverse

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # Get the Customer model from the other app, it can now be used to query the db
    Customer = apps.get_model('customers_addresses.Customer')
    return render(request, 'employees/index.html')


# def register(request):
#     if request.method == 'POST':
#         name = request.method.POST.get('name')
#         zipcode = 0
#         new_employee = Employee(name=name, zip=zipcode)
#         new_employee.save()
#         return HttpResponseRedirect('employee/register.html')
#     else:
#         return render(request, 'employee/register.html')
