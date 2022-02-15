from wsgiref.util import request_uri
from django.db.models.fields import json
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
from .choices import *
from django.utils import timezone
from django.urls import reverse
from django.utils.dateparse import parse_datetime

Users = User.objects.all()

def newComment(request, moduleID, module):
   if "commentContent" in request.POST:
         newComment = Comment(user=request.user, content=request.POST.get("commentContent", False))
         newComment.save()
         CommentLink = module.objects.get(id=moduleID)
         CommentLink.comments.add(newComment)
         CommentLink.save()

def index(request):
   return render(request, "final/index.html")

def tickets(request):
   return render(request, "final/tickets.html", {
      "allTickets": Ticket.objects.all()
   })

def ticketDetails(request, ticketID):
   ticketDetails = Ticket.objects.get(id=ticketID)
   if request.method == "PUT":
      data = json.loads(request.body)
      Ticket.objects.filter(id=ticketID).update(status=data["newStatus"])
      if "Closed" in data["newStatus"] and ticketDetails.status != "Closed":
         Ticket.objects.filter(id=ticketID).update(endDate=timezone.now())
      if data["newStatus"] != "Closed" and ticketDetails.status == "Closed":
         Ticket.objects.filter(id=ticketID).update(endDate=None)
   newComment(request, ticketID, Ticket)
   if "ticketDetailsSubmit" in request.POST:
      Ticket.objects.filter(id=ticketID).update(
         tittle=request.POST["ticketDetailsTittle"],
         priority=int(request.POST["ticketDetailsPriority"]),
         group=request.POST["ticketDetailsGroup"],
         costumer=request.POST["ticketDetailsCostumer"],
         description=request.POST.get("ticketDetailsDescription", False),
         plate=request.POST["ticketDetailsPlate"],
         responsible=request.POST["ticketDetailsResponsible"],
         actionMade=request.POST["ticketDetailsActionMade"],
         analyzedIten=request.POST["ticketDetailsAnalyzedItem"],
         solution=request.POST["ticketDetailsSolution"],
         score=int(request.POST["ticketDetailsPriority"])+int(ticketDetails.costumer.priority)
      )
      return HttpResponseRedirect(reverse("tickets"))

   
   return render(request, "final/tickets.html", {
      "ticketDetails": ticketDetails,
      "ticketStatus": ticketStatusChoices,
      "ticketPriority": priorityChoices,
      "Users": Users,
      "ticketActionMade": ActionMade,
      "ticketAnalyzedItens": AnalyzedItens,
      "ticketGroup": ticketGroup,
      "allCostumers": Costumer.objects.all(),
      })

def servicesOrder(request):
   return render(request, "final/serviceOrder.html", {
      "allServiceOrders": serviceOrder.objects.all()
   })

def serviceOrdersDetails(request, serviceOrderID):
   serviceOrderDetails = serviceOrder.objects.get(id=serviceOrderID)
   newComment(request, serviceOrderID, serviceOrder)
   if request.method == "PUT":
      data = json.loads(request.body)
      serviceOrder.objects.filter(id=serviceOrderID).update(status=data["newStatus"])
      
   if request.method == "POST":
      serviceOrderDetails.costumer = Costumer.objects.get(id=request.POST["serviceOrderDetailsCostumer"]) 
      serviceOrderDetails.tittle = request.POST["serviceOrderDetailsTittle"]
      serviceOrderDetails.plate = request.POST["serviceOrderDetailsPlate"]
      serviceOrderDetails.responsible = User.objects.get(id=request.POST["serviceOrderDetailsResponsible"]) 
      serviceOrderDetails.description = request.POST["serviceOrderDetailsDescription"]
      serviceOrderDetails.schedule = parse_datetime(request.POST["serviceOrderDetailsSchedule"])
      serviceOrderDetails.deliveryDate = parse_datetime(request.POST["serviceOrderDetailsDelivery"])
      serviceOrderDetails.save()

   if "serviceContentSelected" in request.POST:
      data = request.POST.getlist("serviceContentSelected")
      serviceOrderDetails.relatedService.clear()
      for serviceID in data:
         addService = Service.objects.get(id=serviceID)
         serviceOrderDetails.relatedService.add(addService)
         serviceOrderDetails.save()
   elif request.method == "PUT" and "serviceContentSelected" not in request.POST:
      serviceOrderDetails.relatedService.clear()
          
   return render(request,"final/serviceOrder.html", {
      "serviceOrdersDetails": serviceOrderDetails,
      "serviceOrdersStatusChoices": statusOsChoices,
      "allCostumers": Costumer.objects.all(),
      "users": Users,
      "allServices": [svc for svc in Service.objects.all()]
   })

def costumer(request):
   return render(request, "final/costumer.html", {
      "allCostumers": Costumer.objects.all(),
   })

def costumerDetails(request, costumerID):
   newComment(request, costumerID, Costumer)
   if request.method == "POST":
      Costumer.objects.filter(id=costumerID).update(
         type=request.POST.get("costumersDetailsType",""),
         name=request.POST.get("costumersDetailsName",""),
         priority=request.POST.get("costumerDetailsPriority",""),
         phone=request.POST.get("costumersDetailsPhone",""),
         CNPJ=request.POST.get("costumersDetailsCNPJ",""),
         email=request.POST.get("costumersDetailsEmail",""),
         state=request.POST.get("costumersDetailsState",""),
         city=request.POST.get("costumersDetailsCity",""),
         address=request.POST.get("costumersDetailsAddress",""),
         zCode=request.POST.get("costumersDetailsZCode",""),
         )


   return render(request, "final/costumer.html", {
      "costumersDetails": Costumer.objects.get(id=costumerID),
      "costumerTypeChoices": costumerTypeChoices,
      "priorityChoices": priorityChoices
   })

def equipments(request):
   return render(request, "final/equipments.html", {
      "allEquipments": Equipment.objects.all()
   })

def equipmentsDetails(request, equipmentID):
   
   return render(request, "final/equipments.html", {
      "equipmentsDetails": Equipment.objects.get(id=equipmentID),
      "equipmentsDetailsCategories": equipmentCategoriesChoices
   })

def products(request):
   return render(request, "final/products.html", {
      "allProducts": Product.objects.all()
   })

def productsDetails(request, productID):
   
   return render(request, "final/products.html", {
      "productsDetails": Product.objects.get(id=productID)
   })
   

def services(request):
   return render(request, "final/services.html", {
      "allServices": Service.objects.all()
   })
   

def servicesDetails(request, serviceID):
   
   return render(request, "final/products.html", {
      "serviceDetails": Service.objects.get(id=serviceID)
      
   })

def newTicket(request):
   return render(request, "final/newTicket.html")

def newCostumer(request):
   return 0
