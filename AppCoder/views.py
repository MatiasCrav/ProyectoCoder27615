from django.shortcuts import render

from AppCoder.models import Estudiante
from django.http import HttpResponse
from django.template import loader


def inicio(request):
    return render(request, "AppCoder/inicio.html")


def crear_estudiante(request):
    estudiante = Estudiante(
        nombre="Juancito", apellido="Perez", email="juan.perez@gmail.com"
    )
    # Con .save() guardamos la instancia en la bd.
    estudiante.save()
    return HttpResponse(f"Se creó a {estudiante.nombre} {estudiante.apellido}")


def listar_estudiantes(request):
    # Obtengo todos los estudiantes
    estudiantes = Estudiante.objects.all()
    plantilla = loader.get_template("estudiantes.html")
    # Agrego los estudiantes al contexto para usarlos en el html
    mi_contexto = {"estudiantes": estudiantes}
    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)


def curso(request):
    return render(request, "AppCoder/curso.html")


def entregable(request):
    return render(request, "AppCoder/entregable.html")


def estudiante(request):
    return render(request, "AppCoder/estudiante.html")


def profesor(request):
    return render(request, "AppCoder/profesor.html")


# Les dejo una plantilla genérica con bootstrap
def plantilla(request):
    return render(request, "layout.html")