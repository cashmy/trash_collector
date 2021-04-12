from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer
from django.urls import reverse, reverse_lazy
from django.views import generic
from customers_addresses.models import CustomerAddress
from addresses.models import Address
from .forms import CustomerForm, FirstTimeCustomerForm
# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # get the logged in user within any view function
    user = request.user
    # This will be useful while creating a customer to assign the logged in user as the user foreign key
    if not user.is_employee:
        all_customers = Customer.objects.filter(user=user.pk)
        print(all_customers)
        if not Customer.objects.filter(user=user.pk).exists():
            # TODO correct so it only appears when user isnt assigned to anyone
            return redirect('create/', request)
    # Will also be useful in any function that needs
    print(user)
    return render(request, 'customers/index.html')


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
    user = request.user
    new_customer = Customer(name='John Doe', dow='Monday', user=user)
    form = FirstTimeCustomerForm(request.POST or None, request.FILES or None, instance=new_customer)

    if form.is_valid():
        form.save()
        return redirect('index.html')
        # return HttpResponseRedirect(reverse('customers:table'))

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
