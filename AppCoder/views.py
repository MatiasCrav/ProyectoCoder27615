from django.shortcuts import render, redirect

from AppCoder.models import Curso, Estudiante, Profesor, Entregable
from .forms import FormCurso, FormRegistrarse, FormEditarUsuario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


def inicio(request):
    return render(request, "AppCoder/inicio.html")


# Les dejo una plantilla genérica con bootstrap
def plantilla(request):
    return render(request, "AppCoder/layout.html")


# Uso views basadas en funciones para los cursos
@login_required
def cursos(request):
    cursos = Curso.objects.all()
    return render(request, "AppCoder/cursos.html", {"cursos": cursos})


@login_required
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


@login_required
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


@login_required
def eliminar_curso(request, id):
    # Uso Modelo.objects.get(campo=valor) para obtener una instancia de la BD
    curso = Curso.objects.get(id=id)
    curso.delete()
    # Vuelvo a la lista
    return redirect("Cursos")


@login_required
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


@login_required
def ver_curso(request, id):
    curso = Curso.objects.get(id=id)
    return render(request, "AppCoder/ver_curso.html", {"curso": curso})


# Uso CBV para el resto
class ListarEntregables(LoginRequiredMixin, ListView):
    model = Entregable
    template_name = "AppCoder/entregables.html"


class VerEntregable(LoginRequiredMixin, DetailView):
    model = Entregable
    template_name = "AppCoder/ver_entregable.html"


class EditarEntregable(LoginRequiredMixin, UpdateView):
    model = Entregable
    success_url = "/AppCoder/entregables/"
    fields = ["nombre", "fecha", "entregado"]
    # También le podemos decir un template en específico
    template_name = "AppCoder/formEntregable.html"


class CrearEntregable(LoginRequiredMixin, CreateView):
    model = Entregable
    success_url = "/AppCoder/entregables/"
    fields = ["nombre", "fecha", "entregado"]
    # También le podemos decir un template en específico
    template_name = "AppCoder/formEntregable.html"


class EliminarEntregable(LoginRequiredMixin, DeleteView):
    model = Entregable
    success_url = "/AppCoder/entregables/"


@login_required
def entregables(request):
    entregables = Entregable.objects.all()
    return render(request, "AppCoder/entregables.html", {"entregables": entregables})


@login_required
def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, "AppCoder/estudiantes.html", {"estudiantes": estudiantes})


@login_required
def profesores(request):
    profesores = Profesor.objects.all()
    return render(request, "AppCoder/profesores.html", {"profesores": profesores})


def registrarse(request):
    if request.method == "POST":
        form = FormRegistrarse(data=request.POST)
        if form.is_valid():
            form.save()
            # Uso el 'username' del form para obtener el usuario y loguearlo
            username = form.cleaned_data["username"]
            user = User.objects.get(username=username)
            login(request, user)

            # Vuelvo a inicio
            return redirect("Inicio")
        else:
            error = True

    else:
        error = False
        form = FormRegistrarse()

    return render(request, "AppCoder/registrarse.html", {"form": form, "error": error})


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
@login_required
def logout_request(request):
    logout(request)
    return redirect("Inicio")


@login_required
def editar_usuario(request):
    user = request.user
    if request.method == "POST":
        form = FormEditarUsuario(request.POST)
        if form.is_valid():
            info = form.clean_data
            user.username = info["username"]
            user.email = info["email"]
            user.password1 = info["password1"]
            user.password2 = info["password2"]
            user.save()

            # Vuelvo a inicio
            return redirect("Inicio")
        else:
            error = True

    else:
        error = False
        form = FormEditarUsuario(
            initial={"username": user.username, "email": user.email}
        )

    return render(request, "AppCoder/formUsuario.html", {"form": form, "error": error})
