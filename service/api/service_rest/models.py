from django.db import models

# Create your models here.

class Technician(models.Model):
    name = models.CharField(max_length=20)
    employee_number = models.CharField(max_length=20)

class ServiceAppointment(models.Model):
    