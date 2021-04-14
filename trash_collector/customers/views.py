from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer
from django.urls import reverse, reverse_lazy
from django.views import generic
from customers_addresses.models import CustomerAddress
from addresses.models import Address
from .forms import CustomerForm, FirstTimeCustomerForm, CustomerSchedulingForm
import googlemaps
from datetime import datetime
# Create your views here.
# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    user = request.user
    customer = Customer.objects.get(user=user.pk)
    if not user.is_employee:
        if not Customer.objects.filter(user=user.pk).exists():
            # TODO correct so it only appears when user isn't assigned to anyone
            return redirect('create/', request)
        else:
            context = {
                'customer': customer
            }
    form = CustomerSchedulingForm(request.POST or None, instance=customer)
    billing_obj = rtv_customer_address(customer.pk, 'B')
    pickup_obj = rtv_customer_address(customer.pk, 'P')
    context = {
        'customer': customer,
        'form': form,
        'billing_obj': billing_obj,
        'pickup_obj': pickup_obj
    }
    if form.is_valid():
        form.save()

    # Will also be useful in any function that needs
    return render(request, 'customers/index.html', context)


class RegisterView(generic.CreateView):
    """Allows user to register with the custom form we created"""
    form_class = CustomerForm
    success_url = reverse_lazy('index')
    template_name = 'customers/register.html'


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
    form = FirstTimeCustomerForm(request.POST or None, request.FILES or None)
    user = request.user

    if form.is_valid():
        form.save()
        customer = Customer.objects.latest('pk')
        customer.user = user
        customer.save()
        return redirect('index.html')

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


def update(request, customer_id):
    customer_obj = get_object_or_404(Customer, id=customer_id)
    form = CustomerForm(request.POST or None, instance=customer_obj)
    address_list = rtv_all_customer_addresses(customer_id)
    context = {
        'form': form,
        'address_list': address_list
    }
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('customers:table'))

    context['form'] = form
    return render(request, 'customers/update.html', context)


def rtv_customer_address(customer_id, address_type='P'):
    # Address type will be either 'B' for billing or 'P'' for pickup_day
    try:
        address_ref = get_object_or_404(CustomerAddress, address_type=address_type, customer_id=customer_id)
        address_obj = get_object_or_404(Address, id=address_ref.address_id_id)
    except:
        address_obj = ''
    return address_obj


def rtv_all_customer_addresses(customer_id):
    address_obj_list = []
    # Address type will be either 'B' for billing or 'P'' for pickup_day
    try:
        address_ref = CustomerAddress.objects.all().filter(customer_id=customer_id)
        for address in address_ref:
            if address.address_type == 'B':
                address_type_text = 'Billing'
            else:
                address_type_text = 'Pickup'
            address_obj = get_object_or_404(Address, id=address.address_id_id)
            address_obj_item = {
                'address_type_text': address_type_text,
                'address_obj': address_obj,
            }
            address_obj_list.append(address_obj_item)
    except:
        pass
    return address_obj_list


def customer_map(request):
    latitude = 0
    longitude = 0
    context = {
        'latitude': latitude,
        'longitude': longitude
    }
    if request.method == "POST":
        return redirect('index.html')

    return render(request, 'customers/customer_map.html', context)
