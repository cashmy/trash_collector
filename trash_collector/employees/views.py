from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.apps import apps
from .models import Employee
from django.urls import reverse
import datetime
from .forms import FirstTimeEmployeeForm, UpdateZipForm


# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.

def num_to_day(dow):
    switcher = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }
    return switcher.get(dow)


def index(request):  # pass in dictionary exclude dictionary[key] from allcustomers
    Customer = apps.get_model('customers.Customer')
    user = request.user
    # Get the Customer model from the other app, it can now be used to query the db
    if user.is_employee:
        if not Employee.objects.filter(user=user.pk).exists():
            # TODO correct so it only appears when user isnt assigned to anyone
            return redirect('employees:create_new_employee')

    today = datetime.date.today()
    weekday = num_to_day(today.weekday())
    employee = Employee.objects.get(user=user.pk)

    all_customers = Customer.objects.filter(default_pickup_zipcode=employee.assigned_zip_code,
                                            suspension_start_date__gt=today,
                                            dow=weekday
                                            ) | Customer.objects.filter(
        default_pickup_zipcode=employee.assigned_zip_code,
        suspension_end_date__lt=today,
        dow=weekday
    ) | Customer.objects.filter(default_pickup_zipcode=employee.assigned_zip_code,
                                one_time_date=today) | Customer.objects.filter(
        default_pickup_zipcode=employee.assigned_zip_code,
        suspension_start_date=None,
        suspension_end_date=None,
        dow=weekday
        )

    form = UpdateZipForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employees:index')
    context = {'all_customers': all_customers,
               'employee': employee,
               'form': form}
    return render(request, './employees/index.html', context)


def create(request):
    context = {}
    user = request.user
    new_employee = Employee(user=user)
    form = FirstTimeEmployeeForm(request.POST or None, request.FILES or None, instance=new_employee)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('customers:table'))

    context['form'] = form
    return render(request, 'employees/create.html', context)


def completed_pickup(request, customer_id):
    context = {}
    Customer = apps.get_model('customers.Customer')
    customer = Customer.objects.get(pk=customer_id)
    if request.method == "POST":
        customer.current_bill_amount = customer.current_bill_amount + 30
        customer.save()
        return HttpResponseRedirect(reverse('employees:index'))
    context['customer'] = customer
    return render(request, './employees/confirm.html', context)


def preview(request, day):  # day passed in as num
    context = {}
    Customer = apps.get_model('customers.Customer')
    day = num_to_day(day)
    all_customers = Customer.objects.filter(dow=day)
    context['all_customers'] = all_customers
    return render(request, './employees/preview.html', context)


def stop_giving_me_eof_errors():
    pass
