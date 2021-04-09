from django.db import models


# Create your models here.
class Address(models.Model):
    address1 = models.CharField(max_length=50, default='')
    address2 = models.CharField(max_length=50, default='')
    city_name = models.CharField(max_length=50, default='')
    state_code = models.CharField(max_length=2, default='')
    country_code = models.CharField(max_length=2, default='')
    zip_code = models.CharField(max_length=10, default='')
    latitude = models.FloatField(default=0)  # - needed for Google Maps API calls
    longitude = models.FloatField(default=0)  # - needed for Google Maps API calls

    def __str__(self):
        # Possible build a dictionary (object)
        # return the object) - access using key-value pairs
        return self.address1, self.city_name, self.state_code, self.country_code, self.zip_code
