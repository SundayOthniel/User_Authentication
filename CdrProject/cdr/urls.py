from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.logIn, name='login'),
    path('patientrecord', views.patientRecord, name='patientrecord'),
    path('addpatient', views.addPatient, name='addpatient'),
    path('logout', views.logOut, name='logout'),
    path('updatepatient/<int:id>', views.updatePatient, name='updatepatient'),
    path('comfirmdeletepatient/<int:id>', views.comfirmDeletePatient, name='comfirmdeletepatient'),
    path('deletepatient/<int:id>', views.deletePatient, name='deletepatient'),
]