from django.shortcuts import render, redirect
from .forms import AddressForm
# Create your views here.


# def create(request):
#     context = {}
#     form = AddressForm(request.POST or None, request.FILES or None)
#     user = request.user
#     if form.is_valid():
#         form.save()
#
#         return redirect('index.html')
#         # return HttpResponseRedirect(reverse('customers:table'))
#
#     context['form'] = form
#     return render(request, 'customers/create.html', context)
