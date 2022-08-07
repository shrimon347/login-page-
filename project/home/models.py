
from django.db import models

# Create your models here.

class  Employees(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    address = models.TextField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name