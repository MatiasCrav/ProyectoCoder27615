# render es otra forma de cargar templates que veremos en próximas clases
# from django.shortcuts import render

from AppCoder.models import Estudiante
from django.http import HttpResponse
from django.template import loader


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
