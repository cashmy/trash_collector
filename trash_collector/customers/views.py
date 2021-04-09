from django.http import HttpResponse
from django.shortcuts import render
from .models import Customer
# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # get the logged in user within any view function
    user = request.user
    # This will be useful while creating a customer to assign the logged in user as the user foreign key
    # Will also be useful in any function that needs
    print(user)
    return render(request, 'customers/index.html')


def table(request):
    all_customers = Customer.objects.all().orderby('name')
    context = {
        'all_customers': all_customers
    }
    return render(request, 'customers/table.html', context)


def create(request):
    pass


def delete(request, customer_id):
    pass


def update(request, customer_id):
    pass
