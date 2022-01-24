from django.contrib import admin
from django.urls import path, include

from FinalProject.models import serviceOrder
from .. import views

urlpatterns = [
    path("", views.servicesOrder, name="serviceOrder"),
    path("<int:serviceOrderID>", views.serviceOrdersDetails, name="serviceOrdersDetails"),
]