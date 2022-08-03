from django.shortcuts import render
from django.db import models

# Create your views here.
class AutomobileVO(models.Model):
    vin = models.Charfield(max_length=17, unique=True)
    import_href = models.CharField(max_length=200)
    
class SalesPerson(models.Model):
    name = models.CharField(max_length=100)
    employee_number = models.PositiveIntegerField(unique=True)
    
class Customer(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    
class SaleRecord(models.Model):
    price = models.PositiveIntegerField()
    
    automobile = models.ForeignKey(
        AutomobileVO,
        related_name="automobile",
        on_delete=models.PROTECT,
    )
    
    sales_person = models.ForeignKey(
        SalesPerson,
        related_name='+',
        in_delete=models.CASCADE,
    )
    
    customer = models.ForeignKey(
        Customer,
        related_name="customer",
        on_delete=models.CASCADE,
    )
    
    
    
    
    