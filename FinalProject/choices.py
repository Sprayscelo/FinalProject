# Prioridades para Clientes e Chamados

priorityChoices = [

    ("1",1),
    ("2",2),
    ("3",3),
    ("4",4)

]

# Tipo de cliente, Pessoa Fisica ou Juridica

costumerTypeChoices = [

    ("Company Costumer", "Company Costumer"),
    ("Physical Costumer", "Physical Costumer")

]

# Status dos chamados

ticketStatusChoices = [

    ("Open","Open"),
    ("In Progress","In Progress"),
    ("Waiting for response","Waiting for response"),
    ("Escaled", "Escaled"),
    ("Closed", "Closed")

]

# Setores

ticketGroup = [
    ("Support", "Support"),
    ("Financial", "Financial"),
    ("Commercial", "Commercial"),
    ("Services", "Services"),
    ("Administrative", "Administrative"),
    ("Legal", "Legal"),
    ("Stock and Supplies", "Stock and Supplies"),
    ("Development", "Development"),
    ("Costumer Success", "Costumer Success")
]

# Ação realizada Choices

ActionMade = [
    ("Costumer instruction", "Costumer Instruction"),
    ("Register/Update", "Register/Update"),
    ("Validation/Reports", "Validation/Reports"),
    ("Veichle unlock", "Veichle unlock"),
    ("Escaled", "Escaled"),
    ("Reset", "Reset"),
    ("Internal procedure", "Internal procedure")
]

# Itens analisados 

AnalyzedItens = [ 
    ("Antenna - GPS", "Antenna - GSM"),
    ("Antena - GSM", "Antena - GSM"),
    ("CAN", "CAN"),
    ("Sim Card", "Sim Card"),
    ("Equipment", "Equipment"),
    ("Speed Sensor", "Speed Sensor"),
    ("Rpm Sensor", "Rpm Sensor")
]

# Plataformas de atendimento

Plataform = [ 
    ("App Wikidados","App Wikidados"),
    ("Dynamix", "Dynamix"),
    ("Gconnect", "GConnect"),
    ("Getrak", "Getrak"),
    ("Vdoweb", "Vdoweb"),
    ("CRM", "CRM"),
    ("Passanger", "Passanger")

]

# Status dos pedidos de venda

statusOsChoices = [
    ("Created","Created"),
    ("Aproved", "Aproved"),
    ("Waiting for supply","Waiting for supply"),
    ("Waiting for schedule", "Waiting for schedule"),
    ("Scheduled","Scheduled"),
    ("Delivered", "Delivered"),
    ("Billed","Billed"),
    ("Warrantly", "Warrantly"),
    ("Cancelled", "Cancelled")
]

#Categorias dos ativos

equipmentCategoriesChoices = [
    ("Smart", "Smart"),
    ("Premium", "Premium"),
    ("Essential", "Essential"),
    ("Video managment", "Video managment"),
    ("Evolution", "Evolution"),
    ("Silometria", "Silometria"),
    ("OnBoard", "OnBoard")
]

# Operadoras dos chips dos ativos

equipmentsPhoneOperators = [
    ("Algar","Algar"),
    ("Vivo", "Vivo"),
    ("OI", "OI"),
    ("Claro", "Claro"),
    ("TIM", "Tim")
]

# Status dos equipamentos

equipamentsStatus = [
    ("Active","Active"),
    ("Execution", "Execution"),
    ("Stock", "Stock"),
    ("Warrantly", "Warrantly"),
    ("Out of Service", "Out of Service"),
    ("Disabled", "Disabled")
]

# Status dos servicos

serviceStatus = [
    ("Active", "Active"),
    ("Inactive", "Inactive")
]

# Categorias dos servicos

serviceCategories = [
    ("Installation", "Installation"),
    ("Tachograph", "Tachograph"),
    ("Support", "Support"),
    ("Customization", "Customization"),
    ("Training", "Training"),
    ("Access Administration", "Access Adiministration")

]