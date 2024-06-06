from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomAuthenticationForm ,CustomUserCreationForm

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


