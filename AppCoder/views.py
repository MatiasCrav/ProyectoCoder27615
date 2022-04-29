from django.shortcuts import render, redirect

from AppCoder.models import Curso, Estudiante, Profesor, Entregable
from django.http import HttpResponse
from django.template import loader
from .forms import FormCurso


def inicio(request):
    return render(request, "AppCoder/inicio.html")


def cursos(request):
    cursos = Curso.objects.all()
    return render(request, "AppCoder/cursos.html", {"cursos": cursos})


def entregables(request):
    entregables = Entregable.objects.all()
    return render(request, "AppCoder/entregables.html", {"entregables": entregables})


def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, "AppCoder/estudiantes.html", {"estudiantes": estudiantes})


def profesores(request):
    profesores = Profesor.objects.all()
    return render(request, "AppCoder/profesores.html", {"profesores": profesores})


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
            curso = Curso(nombre=informacion["nombre"], comision=informacion["comision"])
            curso.save()
            return redirect("Cursos")
        else:
            # Hubo algún error
            ...

    mi_formulario = FormCurso()
    return render(request, "AppCoder/formCurso.html", {"form": mi_formulario})


def buscar_curso(request):
    if request.GET.get("comision"):
        comision = request.GET["comision"]
        cursos = Curso.objects.filter(comision__icontains=comision)
        return render(
            request,
            "AppCoder/resultadosBusquedaCurso.html",
            {"cursos": cursos, "comision": comision},
        )

    return render(request, "AppCoder/buscarCurso.html")


def eliminar_curso(request, nombre_curso):
    # Uso Modelo.objects.get(campo=valor) para obtener una instancia de la BD
    curso = Curso.objects.get(nombre=nombre_curso)
    curso.delete()
    # Vuelvo a la lista
    return redirect("Cursos")


def editar_curso(request, nombre_curso):
    curso = Curso.objects.get(nombre=nombre_curso)

    if request.method == "POST":
        mi_form = FormCurso(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data

            curso.nombre = info["nombre"]
            curso.comision = info["comision"]

            curso.save()
            return redirect("Cursos")
        else:
            # Hubo algún error
            ...

    print(curso.nombre)
    mi_form = FormCurso(initial={"nombre": curso.nombre, "comision": curso.comision})
    return render(request, "AppCoder/formCurso.html", {"form": mi_form})
