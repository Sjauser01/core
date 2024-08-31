from django.contrib import admin
from .models import Location, Department, Designation, Employee, Level

# Register your models here.
admin.site.register(Location)
admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(Employee)
admin.site.register(Level)