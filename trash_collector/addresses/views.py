from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from .models import Address
from .forms import AddressForm
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
