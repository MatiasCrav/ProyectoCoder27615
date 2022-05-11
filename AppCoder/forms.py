from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Es una clase, va en CapWords
class FormCurso(forms.Form):
    nombre = forms.CharField()
    comision = forms.IntegerField()


class FormRegistrarse(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Repita la contraseña", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class FormEditarUsuario(UserCreationForm):
    email = forms.EmailField(label="Nuevo email")
    password1 = forms.CharField(label="Nueva contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Repita la contraseña", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        help_texts = {k: "" for k in fields}
