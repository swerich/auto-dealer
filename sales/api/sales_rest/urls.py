from django import path 

from .views import (
    api_sales,
    api_customer,
    api_sales_person
)

urlpatterns = [
    path("sales/", api_sales, name="api_sales"),
    path("sales_person/", api_sales_person, name="api_sales_person"),
    path("customers/", api_customer, name="api_customer"),
]