from django.shortcuts import render
from app1.serializers import appointmentSerializer,doctorSerializer,patientSerializer
from app1.models import Patient,Doctor,Appointment
from rest_framework import viewsets

# Create your views here.



class doctorViewSet(viewsets.ModelViewSet):
    queryset=Doctor.objects.all()
    serializer_class=doctorSerializer

class patientViewSet(viewsets.ModelViewSet):
    queryset=Patient.objects.all()
    serializer_class=patientSerializer

class appointmentViewSet(viewsets.ModelViewSet):
    queryset=Appointment.objects.all()
    serializer_class=appointmentSerializer
