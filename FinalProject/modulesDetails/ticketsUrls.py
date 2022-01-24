from django.contrib import admin
from django.urls import path, include

from FinalProject.models import serviceOrder
from .. import views

urlpatterns = [
    path("", views.tickets, name="tickets"),
    path("<int:ticketID>", views.ticketDetails, name="ticketDetails"),
]