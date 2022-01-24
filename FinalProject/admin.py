from django.contrib import admin

from FinalProject.views import equipments
from .models import Comment, Product, Service, User, Costumer, Ticket, serviceOrder, Equipment
# Register your models here.

admin.site.register(User)
admin.site.register(Costumer)
admin.site.register(Ticket)
admin.site.register(serviceOrder)
admin.site.register(Product)
admin.site.register(Equipment)
admin.site.register(Service)
admin.site.register(Comment)