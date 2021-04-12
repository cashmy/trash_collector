from django.shortcuts import render, redirect
from .forms import AddressForm
from .models import Address
from django.apps import apps
# Create your views here.


def create(request):
    context = {}

    form = AddressForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        new_address = Address.objects.latest('pk')
        return redirect('/customer_addresses/create/', new_address)
        # return HttpResponseRedirect(reverse('customers_addresses:table'))

    context['form'] = form
    return render(request, 'addresses/create.html', context)
