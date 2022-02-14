from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="default"),
    path("tickets/", include('FinalProject.modulesDetails.ticketsUrls')),
    path("serviceOrder/", include('FinalProject.modulesDetails.serviceOrdersUrls')),
    path("costumer/", include('FinalProject.modulesDetails.costumersUrls')),
    path("equipments/", include('FinalProject.modulesDetails.equipmentsUrls')),
    path("products/", include('FinalProject.modulesDetails.productsUrls')),
    path("services/", include('FinalProject.modulesDetails.servicesUrls')),

    #API Route
    path("newCostumer", views.newCostumer, name="newCostumer"),
]