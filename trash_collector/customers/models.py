from django.db import models

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', default=0, on_delete=models.CASCADE)
    dow = models.CharField(max_length=9)
    one_time_date = models.DateField(null=True, blank=True)
    suspension_start_date = models.DateField(null=True, blank=True)
    suspension_end_date = models.DateField(null=True, blank=True)
    pickup_charge_amount = models.FloatField(default=0)
    current_bill_amount = models.FloatField(default=0)
    default_currency_code = models.CharField(default='USD', max_length=3)
    default_pickup_zipcode = models.CharField(default='12345', max_length=10)

    def __str__(self):
        return self.name
