from django.urls import path

from service_rest.views import (
    api_delete_service_appointments,
    api_list_service_appointments,
    api_list_service_history,
    api_list_technician
)

urlpatterns = [
    path('service_appointments', api_list_service_appointments, name="list_service_appointments"),
    path('service_appointments/<int:pk>/', api_delete_service_appointments, name="delete_service_appointments"),
    path('technicians/', api_list_technician, name="list_technicians"),
    path('service_history', api_list_service_history, name="list_service_history")
]
