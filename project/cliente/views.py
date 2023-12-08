from datetime import date

from django.shortcuts import redirect, render

from . import models


def home(request):
    clientes = models.Cliente.objects.all()
    context = {"clientes": clientes}
    return render(request, "cliente/index.html", context)


def crear_clientes_varios(request):
    p1 = models.Pais(nombre="Argentina")
    p2 = models.Pais(nombre="Chile")
    p3 = models.Pais(nombre="Uruguay")
    p1.save()
    p2.save()
    p3.save()
    c1 = models.Cliente(nombre="Agustina", apellido="Rios", nacimiento=date(2001, 5, 19), pais_origen=p1)
    c2 = models.Cliente(nombre="Martina", apellido="Imende", nacimiento=date(2003, 9, 25), pais_origen=p2)
    c3 = models.Cliente(nombre="Diana", apellido="Castillo", nacimiento=date(1993, 4, 3), pais_origen=p3)
    c4 = models.Cliente(nombre="Matias", apellido="Lanzetti", nacimiento=date(1990, 6, 10), pais_origen=None)
    c1.save()
    c2.save()
    c3.save()
    c4.save()
    return redirect("cliente:index")


def busqueda(request):
    cliente_nombre = models.Cliente.objects.filter(nombre__contains="agus")

    cliente_nacimiento = models.Cliente.objects.filter(nacimiento__gt=date(2000, 1, 1))

    cliente_pais = models.Cliente.objects.filter(pais_origen=None)

    context = {
        "cliente_nombre": cliente_nombre,
        "cliente_nacimiento": cliente_nacimiento,
        "cliente_pais": cliente_pais,
    }
    return render(request, "cliente/busqueda.html", context)


from . import forms
from django.contrib import messages
from django.urls import reverse
from cliente.forms import ClienteForm

def crear(request):
    if request.method == "post":
        form = ClienteForm(request.POST)
        print(form.errors)  
        if form.is_valid():
            form.save()
            return redirect(reverse("core:index"))
    else:
        form = ClienteForm()

    return render(request, "cliente/crear.html", {"form": form})