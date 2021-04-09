from django.db import models

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', default=0, on_delete=models.CASCADE)
    dow = models.CharField(max_length=9)
    one_time_date = models.DateField()
    suspension_start_date = models.DateField()
    suspension_end_date = models.DateField()
    pickup_charge_amount = models.FloatField()
    current_bill_amount = models.FloatField()
    default_currency_code = models.CharField(max_length=2)
    default_pickup_zipcode = models.CharField(max_length=10)

    def __str__(self):
        return self.name
