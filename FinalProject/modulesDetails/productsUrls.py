from django.contrib import admin
from django.urls import path, include

from FinalProject.models import Costumer
from .. import views

urlpatterns = [
    path("", views.products, name="products"),
    path("<int:productID>", views.productsDetails, name="productsDetails"),
]