from django import forms

# Es una clase, va en CapWords
class FormCurso(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()
