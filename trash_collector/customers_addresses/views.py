from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import CustomerAddress
from django.apps import apps

# Create your views here.


def create(request, address_id):
    context = {}
    Customer = apps.get_model('customers.Customer')
    Address = apps.get_model('Addresses.address')
    customer = Customer.objects.get(user=request.user)
    address = Address.objects.get(pk=address_id)
    if request.method == 'POST':
        is_pickup = request.POST.get('type')
        new_custaddress = CustomerAddress(customer_id=customer,
                                          address_id=address,
                                          address_type=is_pickup)
        new_custaddress.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customer_address/create.html')
