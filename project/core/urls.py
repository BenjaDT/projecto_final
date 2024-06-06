
from django.urls import path
from . import views

app_name= 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/',views.LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path('register/', ... , name='register')
] 