from django import forms


# Es una clase, va en CapWords
class FormCurso(forms.Form):
    nombre = forms.CharField()
    comision = forms.IntegerField()
