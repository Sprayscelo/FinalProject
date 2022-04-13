from tokenize import group
from turtle import title
from urllib import response
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.fields import json
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import JsonResponse
import json
from .choices import *
from django.utils import timezone
from django.urls import reverse
from django.utils.dateparse import parse_datetime
import random

Users = User.objects.all()

def newComment(request, moduleID, module):
   if "commentContent" in request.POST:
         newComment = Comment(user=request.user, content=request.POST.get("commentContent", False))
         newComment.save()
         CommentLink = module.objects.get(id=moduleID)
         CommentLink.comments.add(newComment)
         CommentLink.save()

def logout_view(request):
   logout(request)
   return HttpResponseRedirect(reverse("default"))

def index(request):
   if request.method == "POST":
      email = request.POST["loginEmail"]
      senha = request.POST["loginPassword"]
      loginUser = User.objects.get(email=email)
      user = authenticate(request, username=loginUser.username, password=senha)
      if user is not None:
         login(request, user)
         return HttpResponseRedirect(reverse("tickets"))
      else:
         return render(request, "final/login.html", {
            "message": "Email ou senha invalido"
         })
   else:
      return render(request, "final/login.html")

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
   usuarioAtivo = User.objects.get(username=request.user)
   responsavel = random.choices([int(us.id) for us in Users])
   if request.method == "POST":
      tipoChamado = request.POST["tipoChamado"]
      if int(tipoChamado) in [1,2,3,4,5,6,7]:
         match int(tipoChamado):          
            case 1:
               novoTicket = Ticket(
               tittle="Alteração/Correção de placa",
               priority=1, 
               group=ticketGroup[0], 
               status=ticketStatusChoices[0],
               description=f'Antiga placa: {request.POST["NTAP_placa"]}\n\nNova placa: {request.POST["NTAP_novaPlaca"]}\n\nInformacões adicionais: {request.POST["NTAP_infoAdicional"]}',
               costumer=usuarioAtivo.costumer,
               plate=request.POST["NTAP_placa"],
               responsible=User.objects.get(id=responsavel[0]),
               createdBy=request.user,
               score=sum([1, int(usuarioAtivo.costumer.priority)])
               )
               novoTicket.save()
            
            case 2:
               novoTicket = Ticket(
                  tittle="Alteração/correção de descricao",
                  priority=1,
                  group=ticketGroup[0],
                  status=ticketStatusChoices[0],
                  description=f'Descrição Atual: {request.POST["NTAD_descricao"]}\n\n Nova descricao: {request.POST["NTAD_novaDescricao"]}\n\n Informações Adicionais: {request.POST["NTAD_infoAdicional"]}',
                  costumer=usuarioAtivo.costumer,
                  plate="",
                  responsible=User.objects.get(id=responsavel[0]),
                  createdBy=request.user,
                  score=sum([1, int(usuarioAtivo.costumer.priority)])
               )
               novoTicket.save()
            
            case 3:
               novoTicket = Ticket(
                  tittle="Relatorio de jornada de motorista",
                  priority=1,
                  group=ticketGroup[0],
                  status=ticketStatusChoices[0],
                  description=f'Nome do motorista: {request.POST["NTJ_motorista"]}\n\n De: {request.POST["NTJ_dataDe"]} Até: {request.POST["NTJ_dataAte"]}\n\n O relatório deve ser separado por {request.POST["NTJ_separacao"]}\n\n Informações adicionais: {request.POST["NTJ_infoAdicional"]}',
                  costumer=usuarioAtivo.costumer,
                  plate="",
                  responsible=User.objects.get(id=responsavel[0]),
                  createdBy=request.user,
                  score=sum([1, int(usuarioAtivo.costumer.priority)])
               )
               novoTicket.save()
            
            case 4:
               novoTicket = Ticket(
                  tittle="Alteração de meta de consumo",
                  priority=1,
                  group=ticketGroup[0],
                  status=ticketStatusChoices[0],
                  description=f'Meta desejada: {request.POST["NTAMC_meta"]}\n\nInformações adicionais: {request.POST["NTAMC_infoAdicional"]}\n\n',
                  costumer=usuarioAtivo.costumer,
                  plate=request.POST["NTAMC_placa"],
                  responsible=User.objects.get(id=responsavel[0]),
                  createdBy=request.user,
                  score=sum([1, int(usuarioAtivo.costumer.priority)])
               )
               novoTicket.save()
            
            case 5:
               plat = request.POST.getlist("NTCU_plataforma")
               platString = ", ".join(plat)
               novoTicket = Ticket(
                  tittle="Criação de usuario",
                  priority=1,
                  group=ticketGroup[0],
                  status=ticketStatusChoices[0],
                  description=f'Nome de completo: {request.POST["NTCU_nome"]}\n\nEmail: {request.POST["NTCU_email"]}\n\nPlataforma: {platString}\n\nPermissão de garagem: {request.POST["NTCU_permissaoGaragem"]}\n\nCopiar permissão de: {request.POST["NTCU_copiarPermissao"]}',
                  costumer=usuarioAtivo.costumer,
                  plate="",
                  responsible=User.objects.get(id=responsavel[0]),
                  createdBy=request.user,
                  score=sum([1, int(usuarioAtivo.costumer.priority)])
               )
               novoTicket.save()
            
            case 6:
               novoTicket = Ticket(
                  tittle="Bloqueio de usuario",
                  priority=1,
                  group=ticketGroup[0],
                  status=ticketStatusChoices[0],
                  description=f'E-mail: {request.POST["NTBU_email"]}\n\nPlataformas: {", ".join(request.POST.getlist("NTBU_plataforma"))}\n\nMotivo: {request.POST["NTBU_motivo"]}',
                  costumer=usuarioAtivo.costumer,
                  plate="",
                  responsible=User.objects.get(id=responsavel[0]),
                  createdBy=request.user,
                  score=sum([1, int(usuarioAtivo.costumer.priority)])
               )
               novoTicket.save()
            
            case 7:
               novoTicket = Ticket(
                  tittle="Veiculo sem comunicação",
                  priority=1,
                  group=ticketGroup[0],
                  status=ticketStatusChoices[0],
                  description=f'Veiculo foi utilizado após a ultima data de comunicação?\nR:{request.POST.getlist("NTVC_utilizado")}\n\nSeu veiculo passou por alguma mecanica, auto-eletrica ou qualquer tipo de manutenção recentemente?\n R: {request.POST["NTVC_mecanica"]}\n\nMotivo: {request.POST["NTVC_infoAdicional"]}',
                  costumer=usuarioAtivo.costumer,
                  plate=request.POST["NTVC_placa"],
                  responsible=User.objects.get(id=responsavel[0]),
                  createdBy=request.user,
                  score=sum([1, int(usuarioAtivo.costumer.priority)])
               )
            
            case 8:
               novoTicket = Ticket(
                  tittle="Treinamento",
                  priority=2,
                  group=ticketGroup[0],
                  status=ticketStatusChoices[0],
                  description=f'Data sugerida pelo cliente: {request.POST["NTT_data"]}\n\nPlataformas: {", ".join(request.POST["NTT_plataforma"])}\n\nInformações adicionais:{request.POST["NTT_infoAdicional"]}',
                  costumer=usuarioAtivo.costumer,
                  plate="",
                  responsible=User.objects.get(id=responsavel[0]),
                  createdBy=request.user,
                  score=sum([2, int(usuarioAtivo.costumer.priority)])
               )
            case 9:
               novoTicket = Ticket(
                  tittle="Problemas com relatório",
                  priority=2,
                  group=ticketGroup[0],
                  status=ticketStatusChoices[0],
                  description=f'Relatório: {request.POST["NTPR_tipoRelatorio"]}\n\nPeriodo selecionado: {request.POST["NTPR_periodoDe"]}: até {request.POST["NTPR_periodoAte"]}\n\nVeiculos/motorista ou garagens selecionados:{request.POST["NTPR_garagemPermissao"]}',
                  costumer=usuarioAtivo.costumer,
                  plate="",
                  responsible=User.objects.get(id=responsavel[0]),
                  createdBy=request.user,
                  score=sum([2, int(usuarioAtivo.costumer.priority)])
               )
            case 10:
               novotTicket = Ticket(
                  tittle="Problema de leitura de dados",
                  priority=1,
                  group=ticketGroup[0],
                  status=ticketStatusChoices[0],
                  description=f'Problema de leitura relacionado a {request.POST["NTLD_tipoDados"]}\n\n',
                  costumer=usuarioAtivo.costumer,
                  plate=f'{request.POST["NTLD_placa"]}',
                  responsible=User.objects.get(id=responsavel[0]),
                  createdBy=request.user,
                  score=sum([2, int(usuarioAtivo.costumer.priority)])
               )

            case 11:
               novoTicket = Ticket(
                  title="Procedimentos internos",
                  priority=2,
                  group=ticketGroup[0],
                  status=ticketStatusChoices[0],
                  description=f'Plataformas {", ".join(request.POST.getlist("NTPI_plataforma"))}\n\nDescrição do procedimento: {request.POST["NTPI_descricaoProcedimento"]}',
                  costumer=usuarioAtivo.costumer,
                  responsible=User.objects.get(id=responsavel[0]),
                  createdBy=request.user,
                  score=sum([2, int(usuarioAtivo.costumer.priority)])
               )
            case 12:
               novoTicket = Ticket(
                  
               )

   return render(request, "final/newTicket.html",{
      "Users": Users 
   })

def register(request):
   if request.method == "POST":
      email = request.POST["registerEmail"]
      username = request.POST["registerUsername"]
      password = request.POST["registerPassword"]
      confirmation = request.POST["registerConfirmarPassword"]
      if password != confirmation:
         return render(request, "final/register.html", {
            "message": "As senhas devem ser iguais!"
         })
      try:
         User.objects.get(email=email)
         return render(request, "final/register.html", {
            "message": "Email ja esta em uso"
         })
      except ObjectDoesNotExist:
         user = User.objects.create_user(username, email, password)
         user.save()
         login(request, user)
         return HttpResponseRedirect(reverse("tickets"))
   else:
      return render(request, 'final/register.html')
   
def newCostumer(request):
   return 0
