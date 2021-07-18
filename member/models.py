from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=50) #varchar -> 255
    age = models.IntegerField()
    address = models.TextField(blank=True) #Text 1000

    # model
    # make migration
    # migrate
