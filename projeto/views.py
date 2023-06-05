#Importando a biblioteca httpresponse
from django.http import HttpResponse
import datetime
#importação para manipulação de arquivo externo
from django.template import Template,Context
import xml.etree.cElementTree as ET #essa

#função para abir a pagina cadastro
def cadastro (request):
   documentoExterno = open("C:/Users/rodry/OneDrive/Área de Trabalho/Projeto Final PDA/projeto/projeto/pages/cadastro.html")
   pagina = Template(documentoExterno.read())
   documentoExterno.close()
   ctx = Context()
   documento = pagina.render(ctx)
   return HttpResponse(documento)

#função para abrir a pagina principal
def index (request):
   documentoExterno = open("C:/Users/rodry/OneDrive/Área de Trabalho/Projeto Final PDA/projeto/projeto/pages/index.html")
   pagina = Template(documentoExterno.read())
   documentoExterno.close()
   ctx = Context()
   documento = pagina.render(ctx)
   return HttpResponse(documento)

#função para abrir a pagina login
def login (request):
   documentoExterno = open("C:/Users/rodry/OneDrive/Área de Trabalho/Projeto Final PDA/projeto/projeto/pages/login.html")
   pagina = Template(documentoExterno.read())
   documentoExterno.close()
   ctx = Context()
   documento = pagina.render(ctx)
   return HttpResponse(documento)

def assistente (request):
   documentoExterno = open("C:/Users/rodry/OneDrive/Área de Trabalho/Projeto Final PDA/projeto/projeto/pages/assistente.html")
   pagina = Template(documentoExterno.read())
   documentoExterno.close()
   ctx = Context()
   documento = pagina.render(ctx)
   return HttpResponse(documento)

def combo (request):
   documentoExterno = open("C:/Users/rodry/OneDrive/Área de Trabalho/Projeto Final PDA/projeto/projeto/pages/combo.html")
   pagina = Template(documentoExterno.read())
   documentoExterno.close()
   ctx = Context()
   documento = pagina.render(ctx)
   return HttpResponse(documento)




#função para carregar o xml
#def carregarXML(request):
  #from xml.dom import minidom 
  #documento = ""
  #tree = minidom.parse("C:/Users/rodry/OneDrive/Área de Trabalho/Projeto Final PDA/projeto/projeto/static/exemplo.xml")
  #modelo = tree.getElementsByTagName("food_burguer")
 # for elemento in modelo:
 #    documento += (elemento.attributes['cidade'].value) + "<br>"
  #   return HttpResponse(documento)
  
#    arquivoXML = ET.parse("C:/Users/rodry/OneDrive/Área de Trabalho/Projeto Final PDA/projeto/projeto/static/exemplo.xml")
#    root = arquivoXML.getroot()
#    return HttpResponse("xml")

