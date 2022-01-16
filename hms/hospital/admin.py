from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Condition)
admin.site.register(Patient)
admin.site.register(PatientHistory)
admin.site.register(Schedule)
admin.site.register(EmployeeData)
admin.site.register(Queue)