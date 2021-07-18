from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100) # varchar -> 255
    is_company = models.BooleanField(default=False)
    related_company = models.IntegerField(null=True, blank=True)
    salary = models.DecimalField(decimal_places=2, max_digits=20)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)

class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    street = models.TextField()
    zip = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)