from django.urls import path 

from .views import (
    api_sales,
    api_customer,
    api_sales_person,
    api_sales_person_record,
    api_automobile_vos,
)

urlpatterns = [
    path("sales/", api_sales, name="api_sales"),
    path("sales_person/", api_sales_person, name="api_sales_person"),
    path("automobilevos/", api_automobile_vos, name="api_automobile_vos"),
    path("customers/", api_customer, name="api_customer"),
    path("sales_person_record/<int:sales_person_id>/", api_sales_person_record, name="api_sales_person_record"),
]