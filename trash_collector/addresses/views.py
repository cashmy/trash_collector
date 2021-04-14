from django.shortcuts import render, redirect
from .forms import AddressForm
from .models import Address
from django.apps import apps
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def create(request):
    context = {}
    form = AddressForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        address = Address.objects.latest('pk')
        address.save()
        return redirect('index.html')
        # return HttpResponseRedirect(reverse('customers:table'))

    context['form'] = form
    return render(request, 'addresses/create.html', context)


def update(request, address_id):
    context = {}
    address = Address.objects.get(pk=address_id)
    form = AddressForm(request.POST or None, instance=address)

    if form.is_valid():
        form.save()
        # return redirect('index.html')
        return HttpResponseRedirect(reverse('customers:index'))

    context['form'] = form
    return render(request, 'addresses/update.html', context)
