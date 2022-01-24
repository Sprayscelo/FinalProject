from wsgiref.util import request_uri
from django.db.models.fields import json
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
from .choices import *
from datetime import datetime
from django.utils import timezone
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

Users = User.objects.all()

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
      # Ticket.objects.filter(id=ticketID).update(status=request.POST["newStatus"])
      # if "Closed" in request.POST["newStatus"] and ticketDetails.status != "Closed":
      #    Ticket.objects.filter(id=ticketID).update(endDate=timezone.now())
      # if request.POST["newStatus"] != "Closed" and ticketDetails.status == "Closed":
      #    Ticket.objects.filter(id=ticketID).update(endDate=None)
   if "commentContent" in request.POST:
      newComment = Comment(user=request.user, content=request.POST.get("commentContent", False))
      newComment.save()
      ticketCommentLink = Ticket.objects.get(id=ticketID)
      ticketCommentLink.comments.add(newComment)
      ticketCommentLink.save()
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
      "ticketDetailsScore":int(ticketDetails.priority) + int(ticketDetails.costumer.priority),
      })

def servicesOrder(request):
   return render(request, "final/serviceOrder.html", {
      "allServiceOrders": serviceOrder.objects.all()
   })

def serviceOrdersDetails(request, serviceOrderID):
   serviceOrderDetails = serviceOrder.objects.get(id=serviceOrderID)
   
   if request.method == "PUT":
      data = json.loads(request.body)
      serviceOrder.objects.filter(id=serviceOrderID).update(status=data["newStatus"])
   
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
      "allServices": [svc for svc in Service.objects.all()],
   })

def costumer(request):
   return render(request, "final/costumer.html", {
      "allCostumers": Costumer.objects.all()
   })

def equipments(request):
   return render(request, "final/equipments.html", {
      "allEquipments": Equipment.objects.all()
   })

def products(request):
   return render(request, "final/products.html", {
      "allProducts": Product.objects.all()
   })

def services(request):
   return render(request, "final/services.html", {
      "allServices": Service.objects.all()
   })

#API Route Functions

def newTickets(request):
   return 0

def newCostumer(request):
   return 0

def ticketsAPI(request, ticketID):
   try:
      ticket = Ticket.objects.get(pk=ticketID)
   except Ticket.DoesNotExist:
      return JsonResponse({"error": "Ticket not found."}, status=404)

   if request.method == "GET":
      return JsonResponse(ticket.serialize())