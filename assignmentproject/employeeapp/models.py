from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return self.name