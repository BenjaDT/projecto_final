from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomAuthenticationForm ,CustomUserCreationForm, ImageForm
from .models import Image
# Create your views here.

def index(request):
    return render(request, 'core/index.html')

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'core/login.html'

# falta logout??

def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomUserCreationForm()
    return render(request,'core/register', {'form' : form})


def imagen(request):
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            return render(request,"core/imagen.html",{"obj":obj})
    else:    
        form=ImageForm()
    img=Image.objects.all()
    return render(request,"core/imagen.html",{"img":img,"form":form})
