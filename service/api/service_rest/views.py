from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import AutomobileVO, ServiceAppointment, Technician
from common.json import ModelEncoder
import json
from django.http import JsonResponse
# Create your views here.

class TechnicianEncoder(ModelEncoder):
    model = Technician
    properties = [
        "name",
        "employee_number",
    ]

class AutomobileVOEncoder(ModelEncoder):
    model = AutomobileVO
    properties = [
        "import_href",
        "color",
        "year",
        "vin",
    ]

class ServiceAppointmentEncoder(ModelEncoder):
    model = ServiceAppointment
    properties = [
        "vin",
        "customer",
        "reason",
        "completed",
        "date_time",
        "technician",
        "is_VIP",
    ]
    encoders = {
        "technician": TechnicianEncoder(),
    }

    def get_extra_data(self, o):
        return 

@require_http_methods(["GET", "POST"])
def api_list_service_appointments(request):
    if request.method == "GET":
        service_appointments = ServiceAppointment.objects.all()
        return JsonResponse(
            service_appointments,
            encoder=ServiceAppointmentEncoder,
            safe=False,
        )
    else: #POST
        content = json.loads(request.body)

        try:
            automobile = AutomobileVO.get(import_href=content["automobile"])
            content["automobile"] = automobile
        except AutomobileVO.DoesNotExist:
            return JsonResponse(
                {"message": "invalid bin href"},
                status=400,
            )

        service_appointment = ServiceAppointment.objects.create(**content)
        return JsonResponse(
            service_appointment,
            encoder=ServiceAppointmentEncoder,
            safe=False
        )

@require_http_methods(["DELETE"])
def api_delete_service_appointments(request):
    try:
        service_appointments = ServiceAppointment.objects.get(id=pk)
        service_appointments.delete()
        return JsonResponse(
            service_appointments, 
            encoder=ServiceAppointmentEncoder,
            safe=False
        )
    except ServiceAppointment.DoesNotExist:
        return JsonResponse({"message": "Does not exist"})

@require_http_methods(["GET", "POST"])
def api_list_technician(request):
    if request.method == "GET":
        technician = Technician.objects.all()
        return JsonResponse(
            technician, 
            encoder=TechnicianEncoder, 
            safe=False
        )
    else: #POST
        content = json.loads(request.body)

        technician = Technician.objects.create(**content)
        return JsonResponse(
            technician, 
            encoder=TechnicianEncoder,
            safe=False
        )


@require_http_methods(["GET"])
def api_list_service_history(request):
    if request.method == "GET":
        service_history = ServiceAppointment.vin.objects.all()
        return JsonResponse(
            service_history, 
            encoder=ServiceAppointmentEncoder,
            safe=False
        )

