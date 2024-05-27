
from django.urls import path
from . import views

app_name= 'sucursales'

urlpatterns = [
    path('', views.index, name='index')
]