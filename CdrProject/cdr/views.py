from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import patientRecords
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        surname = request.POST.get('surname')
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = surname
            user.last_name = name
            user.save()
            return redirect('login')
        else:
            return HttpResponse('Mismatched password')

    return render(request, 'register.html')

def logIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('patientrecord')
        else:
            return HttpResponse('Mismatched credentials')
    return render(request, 'login.html')

def logOut(request):
    logout(request)
    return redirect('home')

def patientRecord(request):
    patientrecord = patientRecords.objects.all()
    return render(request, 'patient_record.html', {'patientrecord':patientrecord})

def addPatient(request):
    if request.method == 'POST':
        surename = request.POST.get('surname')
        name = request.POST.get('name')
        age = request.POST.get('age')
        patientrecord = patientRecords(surename=surename, name=name, age=age)
        patientrecord.save()
        return redirect('patientrecord')
    return render(request, 'addpatient.html')

def updatePatient(request, id):
    patientrecord = patientRecords.objects.get(id=id)
    if request.method == 'POST':
        patientrecord.surename = request.POST.get('surname')
        patientrecord.name = request.POST.get('name')
        patientrecord.age = request.POST.get('age')
        patientrecord.save()
        return redirect(reverse('patientrecord'))
    return render(request, 'updatepatient.html', {'patientrecord':patientrecord})

def comfirmDeletePatient(request, id):
    patientrecord = patientRecords.objects.get(id=id)
    return render(request,'deletepatient.html', {'patientrecord':patientrecord})

def deletePatient(request,id):
    patientrecord = patientRecords.objects.get(id=id)
    patientrecord.delete()
    return redirect('patientrecord')
