from django.contrib import admin

# Register your models here.
from .models import Provedor,Producto,Local

admin.site.register(Provedor)
admin.site.register(Producto)
admin.site.register(Local)