from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Customer
from .forms import CustomerForm
from django.urls import reverse, reverse_lazy
from django.views import generic
# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # get the logged in user within any view function
    user = request.user
    # This will be useful while creating a customer to assign the logged in user as the user foreign key
    # TODO COME HERE FOR THE FIRST TIME LOGIN AND REDIRECT FIND USER ON FOREIGN KEY INDEX
    if not user.is_employee:
        pass
    # Will also be useful in any function that needs
    print(user)
    return render(request, 'customers/index.html')


class RegisterView(generic.CreateView):
    """Allows user to register with the custom form we created"""
    form_class = CustomerForm
    success_url = reverse_lazy('index')
    template_name = 'customers/register.html'
# def register(request):
#     if request.method == 'POST':
#         name = request.method.POST.get('name')
#         address = ''
#         pickup_day = request.method.POST.get('pickup')
#
#         new_customer = Customer(name=name, pickup=pickup_day)
#         new_customer.save()
#         return HttpResponse(reverse('customer:index'))
#     else:
#         return render(request, 'customer/register.html')


def table(request):
    all_customers = Customer.objects.all()
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

