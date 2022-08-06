from django.contrib import admin
from.models import AutomobileVO, ServiceAppointment, Customer, Technician
# Register your models here.
class AutomobileVOAdmin(admin.ModelAdmin):
    pass

class CustomerAdmin(admin.ModelAdmin):
    pass

class ServiceAppointmentAdmin(admin.ModelAdmin):
    pass

class TechnicianAdmin(admin.ModelAdmin):
    pass

admin.site.register(AutomobileVO, AutomobileVOAdmin)
admin.site.register(ServiceAppointment, ServiceAppointmentAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Technician, TechnicianAdmin)