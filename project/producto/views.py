from django.shortcuts import render, redirect
from .forms import provedorForm
from .models import Provedor
# Create your views here.

def index(request):
    return render(request, 'producto/index.html')

def provedor_crear(request):
    if request.method == 'POST':
        form = provedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto:provedor_listar')
    else: #get
        form = provedorForm()
    return render(request, 'producto/provedor_crear.html', {'form': form})

def provedor_listar(request):
    consulta = Provedor.objects.all()
    contexto = {'Provedores': consulta}
    return render(request, 'producto/provedor_listar.html', contexto)

def provedor_detalle(request, pk:int):
    consulta = Provedor.objects.get(id=pk)
    context = {"provedor" : consulta}
    return render(request, 'producto/provedor_detalle.html', context)



def provedor_actualizar(request, pk:int):
    consulta = Provedor.objects.get(id=pk)
    if request.method == 'POST':
        form = provedorForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('producto:provedor_listar')
    else: #get
        form = provedorForm(instance=consulta)
    return render(request, 'producto/provedor_actualizar.html', {'form': form})


def provedor_eliminar(request):
    consulta = Provedor.objects.get(id=pk)
    if request.method == 'POST':
        consulta.delete
        return redirect('producto:provedor_listar')
    else:
        return render(request, 'provedor_eliminar.html', {'Provedor':consulta})