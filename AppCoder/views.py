from django.shortcuts import render

from AppCoder.models import Curso, Estudiante
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


def cursos(request):
    return render(request, "AppCoder/cursos.html")


def entregables(request):
    return render(request, "AppCoder/entregables.html")


def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")


def profesores(request):
    return render(request, "AppCoder/profesores.html")


# Les dejo una plantilla genérica con bootstrap
def plantilla(request):
    return render(request, "AppCoder/layout.html")


def crear_curso(request):
    if request.method == "POST":
        curso = Curso(nombre=request.POST["curso"], comision=request.POST["camada"])
        curso.save()
        return render(request, "AppCoder/cursos.html")

    return render(request, "AppCoder/formCurso.html")
