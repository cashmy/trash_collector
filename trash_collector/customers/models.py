from django.db import models

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', default=0, on_delete=models.CASCADE)

    # Weekly pickup DOW
    # one_time pickup date
    # suspension start date
    # suspension end date
    # pickup charge amount
    # current bill amount (?)

    # Billing Address (FK)
    # Default currency code - needed for Paypal API (reference country file)
    # Pickup Address (FK)

    def __str__(self):
        return self.name
