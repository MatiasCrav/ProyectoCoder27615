from django.shortcuts import render, redirect

from AppCoder.models import Curso, Estudiante
from django.http import HttpResponse
from django.template import loader
from .forms import FormCurso


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
        mi_formulario = FormCurso(request.POST)
        
        # .is_valid() chequea que los datos recibidos son validos para los campos
        # definidos en la clase del form. En la diapositiva hay un error: .is_valid()
        # es una función y se llama con () al final.
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], comision=informacion["camada"])
            curso.save()
            return redirect("Cursos")
        else:
            # Hubo algún error
            ...

    mi_formulario = FormCurso()
    return render(request, "AppCoder/formCurso.html", {"form": mi_formulario})
