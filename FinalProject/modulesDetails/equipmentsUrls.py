from django.contrib import admin
from django.urls import path, include

from FinalProject.models import Costumer
from .. import views

urlpatterns = [
    path("", views.equipments, name="equipments"),
    path("<int:equipmentID>", views.equipmentsDetails, name="equipmentsDetails"),
]