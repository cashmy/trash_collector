from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', default=0, on_delete=models.CASCADE)

# TODO: Create an Employee model with properties required by the user stories

    # assigned zip code
    #
