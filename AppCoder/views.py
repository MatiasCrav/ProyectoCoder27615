from django.shortcuts import render, redirect

from AppCoder.models import Curso, Estudiante, Profesor, Entregable
from django.http import HttpResponse
from django.template import loader
from .forms import FormCurso
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout


def inicio(request):
    return render(request, "AppCoder/inicio.html")


# Les dejo una plantilla genérica con bootstrap
def plantilla(request):
    return render(request, "AppCoder/layout.html")


# Uso views basadas en funciones para los cursos
def cursos(request):
    cursos = Curso.objects.all()
    return render(request, "AppCoder/cursos.html", {"cursos": cursos})


def crear_curso(request):
    if request.method == "POST":
        mi_formulario = FormCurso(request.POST)

        # .is_valid() chequea que los datos recibidos son validos para los campos
        # definidos en la clase del form. En la diapositiva hay un error: .is_valid()
        # es una función y se llama con () al final.
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso = Curso(
                nombre=informacion["nombre"], comision=informacion["comision"]
            )
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


def eliminar_curso(request, id):
    # Uso Modelo.objects.get(campo=valor) para obtener una instancia de la BD
    curso = Curso.objects.get(id=id)
    curso.delete()
    # Vuelvo a la lista
    return redirect("Cursos")


def editar_curso(request, id):
    curso = Curso.objects.get(id=id)

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


def ver_curso(request, id):
    curso = Curso.objects.get(id=id)
    return render(request, "AppCoder/ver_curso.html", {"curso": curso})


# Uso CBV para el resto
class ListarEntregables(ListView):
    model = Entregable
    template_name = "AppCoder/entregables.html"


class VerEntregable(DetailView):
    model = Entregable
    template_name = "AppCoder/ver_entregable.html"


class EditarEntregable(UpdateView):
    model = Entregable
    success_url = "/AppCoder/entregables/"
    fields = ["nombre", "fecha", "entregado"]
    # También le podemos decir un template en específico
    template_name = "AppCoder/formEntregable.html"


class CrearEntregable(CreateView):
    model = Entregable
    success_url = "/AppCoder/entregables/"
    fields = ["nombre", "fecha", "entregado"]
    # También le podemos decir un template en específico
    template_name = "AppCoder/formEntregable.html"


class EliminarEntregable(DeleteView):
    model = Entregable
    success_url = "/AppCoder/entregables/"


def entregables(request):
    entregables = Entregable.objects.all()
    return render(request, "AppCoder/entregables.html", {"entregables": entregables})


def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, "AppCoder/estudiantes.html", {"estudiantes": estudiantes})


def profesores(request):
    profesores = Profesor.objects.all()
    return render(request, "AppCoder/profesores.html", {"profesores": profesores})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contra)
            if user:
                login(request, user)
                return redirect("Inicio")

    # Si no me enviaron datos o me los enviaron mal voy al form
    form = AuthenticationForm()
    return render(request, "AppCoder/login.html", {"form": form})


# Puedo usar la funcion logout() de django.contrib.auth para cerrar sesión
def logout_request(request):
    logout(request)
    return redirect("Inicio")