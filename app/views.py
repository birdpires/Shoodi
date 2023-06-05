from django.shortcuts import render

# Create your views here.
def cadastro (request):
    return render(request,'cadastro.html')

#função para abrir a pagina principal
def index (request):
   return render(request,'index.html')

#função para abrir a pagina login
def login (request):
    return render(request,'login.html')
   
  
def combo (request):
    return render(request,'combo.html')