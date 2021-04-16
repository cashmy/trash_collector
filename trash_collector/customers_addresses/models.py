from django.db import models


# Create your models here.
class CustomerAddress(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey('customers.Customer', on_delete=models.CASCADE)
    address_id = models.ForeignKey('addresses.Address', on_delete=models.CASCADE)
    address_type = models.CharField(max_length=1)

    def __str__(self):
        if self.address_type == "P":
            address_string = 'Pickup for ' + str(self.customer_id)
        else:
            address_string = 'Billing for ' + str(self.customer_id)
        return address_string
