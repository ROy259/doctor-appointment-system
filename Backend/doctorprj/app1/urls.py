from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app1.views import doctorViewSet, patientViewSet, appointmentViewSet

router = DefaultRouter()
router.register(r'doctors', doctorViewSet)
router.register(r'patients', patientViewSet)
router.register(r'appointments', appointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
