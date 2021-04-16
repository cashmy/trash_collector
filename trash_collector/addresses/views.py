from django.shortcuts import render, redirect
from .forms import AddressForm
from .models import Address
from customers.models import Customer
from customers_addresses.models import CustomerAddress
from django.apps import apps
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import requests


# Create your views here.
def create(request, customer_id, address_type):
    context = {}
    form = AddressForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        # rtv lat & long
        lat_long = get_lat_long(request, address)
        address.latitude = lat_long['results'][0]['geometry']['location']['lat']
        address.longitude = lat_long['results'][0]['geometry']['location']['lng']
        address.save()
        # Now add to the join table
        customer_obj = Customer.objects.get(pk=customer_id)
        customer_address = CustomerAddress(address_type=address_type,
                                           address_id=form.instance,
                                           customer_id=customer_obj)
        customer_address.save()
        return HttpResponseRedirect(reverse('customers:index'))
        # return HttpResponseRedirect(reverse('customers:table'))

    context['form'] = form
    return render(request, 'addresses/create.html', context)


def update(request, address_id):
    context = {}
    address = Address.objects.get(pk=address_id)
    form = AddressForm(request.POST or None, instance=address)

    if form.is_valid():
        form.save()
        # Update lat & long
        lat_long = get_lat_long(request, address)
        address.latitude = lat_long['results'][0]['geometry']['location']['lat']
        address.longitude = lat_long['results'][0]['geometry']['location']['lng']
        address.save()
        return HttpResponseRedirect(reverse('customers:index'))

    context['form'] = form
    return render(request, 'addresses/update.html', context)


def get_lat_long(request, address):
    # address_obj = rtv_customer_address(customer_id)
    geo_address = address.address1 + '+' + address.city_name + '+' + address.state_code + '+' + address.zip_code
    geo_string = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + geo_address + '&key=AIzaSyDMAD9fxsFUUm9AZi85Hlf9YtLDLt-nPrk'
    response = requests.get(geo_string)
    address_info = response.json()
    print(address_info['results'][0]['formatted_address'])
    return address_info
