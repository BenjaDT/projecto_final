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

def provedor_actualizar(request):
    ...