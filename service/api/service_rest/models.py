from turtle import color
from django.db import models

# Create your models here.

class AutomobileVO(models.Model):
    import_href = models.CharField(max_length=200, unique=True)
    color = models.CharField(max_length=50)
    year = models.PositiveSmallIntegerField()
    vin = models.CharField(max_length=17, unique=True)

class Customer(models.Model):
    name = models.CharField(max_length=20)

class Technician(models.Model):
    name = models.CharField(max_length=20)
    employee_number = models.CharField(max_length=3)

class ServiceAppointment(models.Model):
    vin = models.CharField(max_length=17)
    customer = models.ForeignKey(Customer, related_name="service_appointment", on_delete=models.PROTECT)
    reason = models.TextField()
    completed = models.BooleanField(default=False)
    date_time = models.DateTimeField(auto_now_add=True)
    technician = models.ForeignKey(Technician, related_name="service_appointment", on_delete=models.PROTECT, null=True)
    is_VIP = models.BooleanField(default=False)