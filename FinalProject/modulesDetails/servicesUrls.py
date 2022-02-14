from django.contrib import admin
from django.urls import path, include

from FinalProject.models import Costumer
from .. import views

urlpatterns = [
    path("", views.services, name="services"),
    path("<int:serviceID>", views.servicesDetails, name="servicesDetails"),
]