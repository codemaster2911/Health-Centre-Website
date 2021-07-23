from django.contrib import admin
from home.models import Appointment, Doctors,Patient,book_appointment
# Register your models here.
admin.site.register(Doctors)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','email','speciality')
    
admin.site.register(Appointment)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','doctor_name','patient_name','date')
    
admin.site.register(Patient)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','email','blood_group')
    
admin.site.register(book_appointment)
