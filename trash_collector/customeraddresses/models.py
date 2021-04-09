from django.db import models


# TODO: Change customer cascade to null on address delete

# Create your models here.
class CustomerAddress(models.Model):
    customer_id = models.ForeignKey('customers.id', on_delete=models.SET_NULL)
    address_id = models.ForeignKey('address.id', on_delete=models.CASCADE)
