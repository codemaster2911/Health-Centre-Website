from django.db import models
from django.db.models.fields import CharField
# Create your models here.
class Doctors(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=100)
    speciality=models.CharField(max_length=30)
    
class Appointment(models.Model):
    doctor_name=models.CharField(max_length=30)
    patient_name=models.CharField(max_length=30)
    date=models.CharField(max_length=30)

class Patient(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=100)
    blood_group=models.CharField(max_length=30)
    
class book_appointment(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    dob=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    desc=models.CharField(max_length=30)