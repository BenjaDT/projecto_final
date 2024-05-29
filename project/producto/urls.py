
from django.urls import path
from . import views

app_name= 'producto'

urlpatterns = [
    path('', views.index, name='index'),
    path('provedor/crear', views.provedor_crear, name='provedor_crear'), #solo deberia ser accesible por admin
    path('provedor/listar', views.provedor_listar, name='provedor_listar'),
    #path('provedor/actualizar', views.provedor_actualizar, name='provedor_actualizar'), #solo deberia ser accesible por admin
]