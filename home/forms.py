from django.core import validators
from django import forms
from django.db.models import fields
from home.models import Doctors,Appointment,Patient

class DoctorRegistration(forms.ModelForm):
    class Meta:
        model=Doctors
        fields=['name','email','speciality']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'speciality':forms.TextInput(attrs={'class':'form-control'}),
        }
        
class AppointmentRegistration(forms.ModelForm):
    class Meta:
        model=Appointment
        fields=['doctor_name','patient_name','date']
        widgets={
            'doctor_name':forms.TextInput(attrs={'class':'form-control'}),
            'patient_name':forms.TextInput(attrs={'class':'form-control'}),
            'date':forms.TextInput(attrs={'class':'form-control'}),
        }
        
        
class PatientRegistration(forms.ModelForm):
    class Meta:
        model=Patient
        fields=['name','email','blood_group']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'blood_group':forms.TextInput(attrs={'class':'form-control'}),
        }