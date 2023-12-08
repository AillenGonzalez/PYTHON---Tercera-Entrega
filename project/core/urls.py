from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="index"),
    path("about/", views.about, name="about"),
    path("cliente/", views.cliente, name="cliente"),
    path("buscar/", views.buscar_view, name="buscar"),
   
]
