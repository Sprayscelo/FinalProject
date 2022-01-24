from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="default"),
    path("tickets/", include('FinalProject.modulesDetails.ticketsUrls')),
    path("serviceOrder/", include('FinalProject.modulesDetails.serviceOrdersUrls')),
    path("costumer", views.costumer, name="costumer"),
    path("equipments", views.equipments, name="equipments"),
    path("products", views.products, name="products"),
    path("services", views.services, name="services"),

    #API Route
    path("newTickets", views.newTickets, name="newTickets"),
    path("newCostumer", views.newCostumer, name="newCostumer"),
]