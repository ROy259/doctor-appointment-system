from django.contrib import admin
from app1.models import Appointment,Doctor,Patient

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Doctor)
admin.site.register(Patient)