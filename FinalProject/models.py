from datetime import time
from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField, DateTimeField
from django.utils import timezone
from .choices import *
import datetime

class Costumer(models.Model):
    
    type = models.CharField(max_length=255, choices=costumerTypeChoices)
    name = models.CharField(max_length=255, blank=False)
    priority = models.CharField(choices=priorityChoices, default=1, max_length=1)
    phone = models.CharField(max_length=11, blank=True, null=True)
    CNPJ = models.CharField(blank=False, max_length=14, unique=True)
    email = models.EmailField(max_length=255, blank=False, unique=True)
    createDate = models.DateField(auto_now_add=True)
    state = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=50, default="")
    zCode = models.CharField(max_length=8, default="")

    def __str__(self):
        return f"{self.name}"

class User(AbstractUser):
    costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE, default="", blank=True, null=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    content = models.TextField(default="")
    createDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        formatDate = self.createDate.strftime('%d/%m/%Y - %H:%M:%S')
        return f"{self.user} | {self.content} | Related Tickets ID`s: {[i.id for i in self.relatedTicket.all()]} | Created at {formatDate}"

class Ticket(models.Model):
    tittle = models.CharField(max_length=30, default="")
    priority = models.CharField(choices=priorityChoices, max_length=1)
    group = models.CharField(max_length=255, choices=ticketGroup, default="Support")
    status = models.CharField(max_length=255,choices=ticketStatusChoices, default="Open")
    description = models.TextField(blank=False)
    costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE, related_name="ticketCostumer")
    plate = models.CharField(max_length=8, default="")
    responsible = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ticketResponsible", null=True, blank=True)
    createDate = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ticketCreator")
    endDate = models.DateTimeField(blank=True, null=True)
    analyzedIten = models.CharField(choices=AnalyzedItens, max_length=255, default="")
    actionMade = models.CharField(choices=ActionMade, max_length=255, default="")
    plataform = models.CharField(choices=Plataform, max_length=255, default="")
    solution = models.TextField(default="")
    score = models.IntegerField(default=0)
    document = models.FileField(null=True, blank=True, upload_to=f'ticket/')
    comments = models.ManyToManyField(Comment, default="", blank=True, related_name="relatedTicket")

    def __str__(self):
        self.document = models.FileField(null=True, blank=True, upload_to=f'ticket/{self.id}')
        return f"ID:{self.id} | Tittle: {self.tittle} | Costumer: {self.costumer} | Responsible: {self.responsible}"
    
    def serialize(self):
        return {
            "tittle": self.tittle,
            "priority": self.priority,
            "status": self.status,
            "description": self.description,
            "costumer": self.costumer.clientName,
            "plate": self.plate,
            "comments": self.comment,
            "responsible": self.responsible.user_name,
            "createDate": self.createDate.strftime("%m/%d/%Y, %H:%M:%S"),
            "createdBy": self.createdBy.user_name,
            "endDate": self.endDate
        }

class Service(models.Model):
    name = models.CharField(max_length=50, default="")
    status = models.CharField(max_length=50, choices=serviceStatus)
    categorie = models.CharField(max_length=50, choices=serviceCategories)
    price = models.FloatField()
    description = models.TextField(default="")
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True)
    comments = models.ManyToManyField(Comment, default="", blank=True, related_name="relatedServices")
    
    def __str__(self):
        return f"Service Name: {self.name} | Categorie:{self.categorie} | Price: {self.name}"

class Product(models.Model):
    name = models.CharField(max_length=255, default="")
    serialNumber = models.CharField(max_length=255, default="")
    brand = models.CharField(max_length=20, default="")
    categories = models.CharField(choices=equipmentCategoriesChoices, max_length=50, default="")
    producer = models.CharField(max_length=30, default="", blank=False)
    description = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comment, default="", blank=True, related_name="relatedProducts")

    def __str__(self):
        return f"{self.name}"
   
class Equipment(models.Model):
    type = models.CharField(choices=equipmentCategoriesChoices, max_length=254)
    costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE, default="", blank=True)
    plate = models.CharField(max_length=8, default="")
    notes = models.TextField(default="", blank=True)
    serialNumber = models.CharField(max_length=30)
    phoneOperator = models.CharField(choices=equipmentsPhoneOperators, max_length=30)
    chip = models.CharField(max_length=20)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(choices=equipamentsStatus, max_length=30)
    inUseDate = DateTimeField(blank=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    relatedSo = models.ManyToManyField(Product, related_name="relatedServiceOrder")
    relatedTicket = models.ManyToManyField(Ticket, default="", related_name="relatedTicket")
    comments = models.ManyToManyField(Comment, default="", blank=True, related_name="relatedEquipments")
        
class serviceOrder(models.Model):
    tittle = models.CharField(max_length=30, default="")
    status = models.CharField(choices=statusOsChoices, max_length=50, default="")
    description = models.TextField(blank=True)
    costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    plate = models.CharField(max_length=8, default="")
    responsible = models.ForeignKey(User, on_delete=models.CASCADE, related_name="osResponsible")
    createDate = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name="osCreator")
    schedule = models.DateTimeField(blank=True, null=True)
    deliveryDate = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    relatedTicket = models.ManyToManyField(Ticket, related_name="ticketRelated")
    relatedService = models.ManyToManyField(Service, related_name="serviceRelated")
    relatedEquipment = models.ManyToManyField(Equipment, blank=True, related_name="equipmentRelated")
    comments = models.ManyToManyField(Comment, default="", blank=True, related_name="relatedServiceOrder")
     
    def __str__(self):
        return f"{self.tittle} - Plate: {self.plate} - Produto: {self.product} - Created at {self.createDate}"

