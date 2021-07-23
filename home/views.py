# from home.forms import DoctorRegistration
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from home.forms import DoctorRegistration,AppointmentRegistration,PatientRegistration
from home.models import Doctors,Appointment,Patient,book_appointment
# Create your views here.
def home(request):
    return render(request,'home.html')

def vd(request):
    return render(request,'vd.html')

def service(request):
    return render(request,'service.html')

def phome(request):
    return render(request,'phome.html')

def pappointment(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        dob=request.POST['dob']
        gender=request.POST['gender']
        ins = book_appointment(fname=fname,lname=lname,email=email,phone=phone,desc=desc,dob=dob,gender=gender)
        ins.save()
        messages.success(request,'Your request has been succesfully saved.Appointment details will be sent to your registered Email id')
        return redirect('pappointment')
    return render(request,'pappointment.html')

def doctors(request):
    if request.method=='POST':
        fm=DoctorRegistration(request.POST)
        if fm.is_valid:
            fm.save()
        fm=DoctorRegistration()
    else:
        fm=DoctorRegistration()
    stud=Doctors.objects.all()
    return render(request,'doctors.html',{'form':fm,'stu':stud})
    
def delete_data(request,id):
    if request.method=='POST':
        pi=Doctors.objects.get(pk=id)
        pi.delete()
        return redirect('doctors')

def update_data(request,id):
    if request.method=='POST':
        pi=Doctors.objects.get(pk=id)
        fm=DoctorRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        messages.success(request,'Update was successful')
    else:
        pi=Doctors.objects.get(pk=id)
        fm=DoctorRegistration(instance=pi)
    return render(request,'updateDoctor.html',{'form':fm,'id':id})

def handleSignup(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        
        if password!=cpassword:
            messages.error(request,"Password do not match")
            return redirect('home')
        
        myuser=User.objects.create_user(name,email,password)
        myuser.save()
        messages.success(request,"Your account has been succesfully created")
        return redirect('home')
    else:
        return HttpResponse('NOT ALLOWED')
    
    
    
def handleLogin(request):
    if request.method=='POST':
        username=request.POST['username']
        lpassword=request.POST['lpassword']
        
        user=authenticate(username=username,password=lpassword)
        
        if user is not None:
            login(request,user)
            messages.success(request,'Login was successful')
            return redirect('home')
        else:
            messages.error(request,'Invalid Credantials,Please Try Again')
            return redirect('home')
        
    return HttpResponse('404-NOT FOUND')


def handleLogout(request):
    logout(request)
    messages.success(request,'Logout was successful')
    return redirect('home')
    
    return HttpResponse('handleLogout')

def appointment(request):
    if request.method=='POST':
        fm=AppointmentRegistration(request.POST)
        if fm.is_valid:
            fm.save()
        fm=AppointmentRegistration()
    else:
        fm=AppointmentRegistration()
    stud=Appointment.objects.all()
    return render(request,'appointment.html',{'form':fm,'stu':stud})

def delete_data2(request,id):
    if request.method=='POST':
        pi=Appointment.objects.get(pk=id)
        pi.delete()
        return redirect('appointment')
    
def update_data2(request,id):
    if request.method=='POST':
        pi=Appointment.objects.get(pk=id)
        fm=AppointmentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        messages.success(request,'Update was successful')
    else:
        pi=Appointment.objects.get(pk=id)
        fm=AppointmentRegistration(instance=pi)
    return render(request,'updateAppointment.html',{'form':fm,'id':id})

def patient(request):
    if request.method=='POST':
        fm=PatientRegistration(request.POST)
        if fm.is_valid:
            fm.save()
        fm=PatientRegistration()
    else:
        fm=PatientRegistration()
    stud=Patient.objects.all()
    return render(request,'patient.html',{'form':fm,'stu':stud})

def delete_data3(request,id):
    if request.method=='POST':
        pi=Patient.objects.get(pk=id)
        pi.delete()
        return redirect('patient')
    
def update_data3(request,id):
    if request.method=='POST':
        pi=Patient.objects.get(pk=id)
        fm=PatientRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        messages.success(request,'Update was successful')
    else:
        pi=Patient.objects.get(pk=id)
        fm=PatientRegistration(instance=pi)
    return render(request,'updatePatient.html',{'form':fm,'id':id})

def index(request):
    return render(request,'index.html')
