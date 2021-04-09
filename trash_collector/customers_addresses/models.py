from django.db import models


# Create your models here.
class CustomerAddress(models.Model):
    customer_id = models.ForeignKey('customers.id', on_delete=models.SET_NULL)
    address_id = models.ForeignKey('address.id', on_delete=models.CASCADE)
    address_type = models.CharField(max_length=1, primary_key=True)