from django.contrib import admin
from api.models import  Employee
# Register your models here.

class EmpolyeeAdmin(admin.ModelAdmin):
    list_display= ('Employee_name','Employee_role')

admin.site.register(Employee,EmpolyeeAdmin)
