from django.contrib import admin
from . models import Absence, DemandAbsence

# Register your models here.


admin.site.register(Absence)
admin.site.register(DemandAbsence)