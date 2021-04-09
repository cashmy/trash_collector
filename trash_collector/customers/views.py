from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Customer
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
    context = {}
    context["customer"] = Customer.objects.get(id=customer_id)
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

