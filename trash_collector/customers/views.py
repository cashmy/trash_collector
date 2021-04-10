from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Customer
from customers_addresses.models import CustomerAddress
from addresses.models import Address
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .forms import CustomerForm
# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # get the logged in user within any view function
    user = request.user
    # This will be useful while creating a customer to assign the logged in user as the user foreign key
    # Will also be useful in any function that needs
    print(user)
    return render(request, 'customers/index.html')


def register(request):
    if request.method == 'POST':
        name = request.method.POST.get('name')
        address = ''
        pickup_day = request.method.POST.get('pickup')

        new_employee = Employee(name=name, pickup=pickup_day)
        new_employee.save()
        return HttpResponse(reverse('customer:index'))
    else:
        return render(request, 'customer/register.html')


def table(request):
    all_customers = Customer.objects.all()
    context = {
        'all_customers': all_customers
    }
    return render(request, 'customers/table.html', context)


def detail(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    billing_obj = rtv_customer_address(customer_id, 'B')
    pickup_obj = rtv_customer_address(customer_id, 'P')
    context = {
        'customer': customer,
        'billing_obj': billing_obj,
        'pickup_obj': pickup_obj
    }
    if request.method == 'POST':
        return HttpResponseRedirect(reverse('customers:table'))
    else:
        return render(request, 'customers/detail.html', context)


def create(request):
    context = {}
    form = CustomerForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('customers:table'))

    context['form'] = form
    return render(request, 'customers/create.html', context)


def delete(request, customer_id):
    context = {}

    # fetch the object related to passed id
    customer_obj = get_object_or_404(Customer, id=customer_id)

    if request.method == "POST":
        # delete object
        customer_obj.delete()
        # after deleting redirect to
        # table(list) page
        return HttpResponseRedirect(reverse('customers:table'))
    context['customer'] = customer_obj
    return render(request, 'customers/delete.html', context)
    pass


def update(request, customer_id):
    context = {}
    customer_obj = get_object_or_404(Customer, id=customer_id)
    form = CustomerForm(request.POST or None, instance=customer_obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('customers:table'))

    context['form'] = form
    return render(request, 'customers/update.html', context)


def rtv_customer_address(customer_id, address_type='P'):
    # Address type will be either 'B' for billing or 'P'' for pickup_day
    address_ref = get_object_or_404(CustomerAddress, address_type=address_type, customer_id=customer_id)
    address_obj = get_object_or_404(Address, id=address_ref.address_id_id)
    return address_obj
