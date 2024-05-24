from django.http import HttpResponse
from django.shortcuts import render

def probando_template(request):
    datos = {"saludo":"Bienvenido a Señora Vaca"}
    return render(request, 'home.html', context=datos)