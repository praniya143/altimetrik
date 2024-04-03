from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator

class CustomUser(AbstractUser):
    pass

class Manufacturer(models.Model):
    name = models.CharField(max_length=50)

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    date_of_manufacture = models.DateField()
    waranty_information = models.TextField(null=True)    

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['serial_number'], name='Serial Number')
        ]
