from django.shortcuts import render
from django.db import models
from common.json import ModelEncoder
from django.http import JsonResponse
import json

from .models import AutomobileVO, SaleRecord, SalesPerson, Customer
from django.views.decorators.http import require_http_methods 

# Create your views here.

class SalesPersonEncoder(ModelEncoder):
    model = SalesPerson
    properties = [
        "name",
        "employee_number",
        "id",
    ]

class AutomobileVOEncoder(ModelEncoder):
    model = AutomobileVO
    properties = [
        "id",
        "vin",
    ]
    
class CustomerEncoder(ModelEncoder):
    model = Customer
    properties = [
        "id",
        "name",
    ]
    
    
class SaleRecordEncoder(ModelEncoder):
    model = SaleRecord
    properties = [
        "vin",
        "customer",
        "price",
        "sales_person",
        "id",
    ]
    encoders = {
        "automobile": AutomobileVOEncoder(),
        "customer": CustomerEncoder(),
        "sales_person": SalesPersonEncoder(),
        
    }
    

    
    
    
@require_http_methods(["GET", "POST"])
def api_sales(request):
    if request.method == "GET":
        sales = SaleRecord.objects.all()
        return JsonResponse(
            {"sales": sales},
            encoder=SaleRecordEncoder,
        )
    else:
        try:
            content = json.loads(request.body)
            
            automobile_id = content["automobile_vo_id"]
            automobile = AutomobileVO.objects.get(pk=automobile_id)
            content["automobile"] = automobile 
            
            customer_id = content["customer_id"]
            customer = Customer.objects.get(pk=customer_id)
            content["customer"] = customer 
            
            sales_person_id = content["sales_person_id"]
            sales_person = SalesPerson.objects.get(pk=sales_person_id)
            content["sales_person"] = sales_person 
            
            sales = SaleRecord.objects.create(**content)
            return JsonResponse(
                sales,
                encoder=SaleRecordEncoder,
                safe=False,
            )
        except:
            response = JsonResponse(
                {"Message": "Could not create a sale record"}
            )
            response.status_code = 400,
            return response
            
            
            
@require_http_methods(["GET", "POST"])
def api_sales_person(request):
    if request.method == "GET":
        sales_person = SalesPerson.objects.all()
        return JsonResponse(
            {"sales_person": sales_person},
            encoder=SalesPersonEncoder,
            safe=False,
        )
    else:
        try:
            content = json.loads(request.body)
            sales_person = SalesPerson.objects.create(**content)
            return JsonResponse(
                sales_person,
                encoder=SalesPersonEncoder,
                safe=False,
            )
        except:
            response = JsonResponse(
                {"Message": "Could not create a sales person"}
            )
            response.status_code = 400
            return response 
        
        
@require_http_methods(["GET", "POST"])
def api_customer(request):
    if request.method == "GET":
        customers = Customer.objects.all()
        return JsonResponse(
            {"Customers": customers},
            encoder=CustomerEncoder,
        )
    else:
        try:
            content = json.loads(request.body)
            customer = Customer.objects.create(**content)
            return JsonResponse(
                customer,
                encoder=CustomerEncoder,
                safe=False
            )
        except:
            response = JsonResponse(
                {"Message": "Could not create a customer"}
            )
            response.status_code = 400
            return response
        
            

            
            
            