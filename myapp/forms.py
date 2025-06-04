from django import forms
from .models import Ganado_Vacuno

class Ganado_Vacuno_Form(forms.ModelForm):
    class Meta:
        model = Ganado_Vacuno
        fields = ["codigo_arete", "raza", "color", "sexo", "lugar_origen", "precio_por_kilo",
                  "estaVivo", "fecha_nacimiento", "fecha_compra"]
        widgets = {
            'codigo_arete': forms.TextInput(attrs={"class": "form-control mt-2"}),
            'raza': forms.TextInput(attrs={"class": "form-control mt-2"}),
            'color': forms.TextInput(attrs={"class": "form-control mt-2"}),
            'sexo': forms.TextInput(attrs={"class": "form-control mt-2"}),
            'lugar_origen': forms.TextInput(attrs={"class": "form-control mt-2"}),
            'precio_por_kilo': forms.TextInput(attrs={"class": "form-control mt-2"}),
            'estaVivo': forms.CheckboxInput(attrs={"class": "form-check-input ms-3 mt-2"}),
            'fecha_nacimiento': forms.TextInput(attrs={"class": "form-control mt-2"}),
            'fecha_compra': forms.TextInput(attrs={"class": "form-control mt-2"}),
        }