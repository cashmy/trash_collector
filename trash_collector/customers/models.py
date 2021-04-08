from django.db import models
# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', default=0, on_delete=models.CASCADE)

    # Weekly pickup DOW
    # one_time pickup date
    # pickup charge amount
    # current bill amount (?)
    # suspension start date
    # suspension end date

    # Billing Address (FK)
    # Pickup Address (FK)
