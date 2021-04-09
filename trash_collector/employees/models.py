from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', default=0, on_delete=models.CASCADE)
    assigned_zip_code = models.CharField(max_length=10)

    def __str__(self):
        return self.name
