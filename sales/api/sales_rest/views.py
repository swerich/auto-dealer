from django.shortcuts import render
from django.db import models
from common.json import ModelEncoder

from .models import AutomobileVO, SaleRecord, SalesPerson, Customer
from django.views.decorators.http import require_http_methods 

# Create your views here.

class SalesPersonEncoder(ModelEncoder):
    model = SalesPerson
    properties = [
        "name",
        "employee_number",
    ]

class SaleRecordEncoder(ModelEncoder):
    model = SaleRecord
    
class SaleRecordEncoder(ModelEncoder):
    model = SaleRecord 
    
class AutomobileVOEncoder(ModelEncoder):
    model = AutomobileVO