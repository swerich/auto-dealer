from django.contrib import admin
from .models import AutomobileVO, Customer, SalesPerson, SaleRecord

# Register your models here.
class AutomobileVOAdmin(admin.ModelAdmin):
    pass

class CustomerAdmin(admin.ModelAdmin):
    pass

class SalesPersonAdmin(admin.ModelAdmin):
    pass

class SaleRecordAdmin(admin.ModelAdmin):
    pass

admin.site.register(AutomobileVO, AutomobileVOAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(SalesPerson, SalesPersonAdmin)
admin.site.register(SaleRecord, SaleRecordAdmin)
