from rest_framework import serializers
from .models import Appointment,Doctor,Patient






class doctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields='__all__'

class patientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields='__all__'

class appointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Appointment
        fields='__all__'