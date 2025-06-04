from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.http import HttpResponse
from django.http.response import JsonResponse
from .forms import Ganado_Vacuno_Form
from .models import Ganado_Vacuno
import random

# Página de inicio.
def inicio(request):
    return render(request, "inicio.html")

# Página de registro.
def signup(request):
    if request.method == "GET":
        return render(request, "signup.html", {
            "form": UserCreationForm
        })
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                # Registrar usuario
                user = User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect("dashboard")
            except IntegrityError:
                print("Error: Usuario en existencia.")
                return render(request, "signup.html", {
                    "form": UserCreationForm,
                    "error": "Error: Usuario en existencia."
                })
        
        print("Error: Las contraseñas no coinciden.")
        return render(request, "signup.html", {
            "form": UserCreationForm,
            "error": "Error: Las contraseñas no coinciden."
        })
    
# Menú del dashboard
def dashboard(request):
    return render(request, "dashboard.html")

# Salir de la sesión
def logoutPage(request):
    logout(request)
    return redirect("inicio")

# Iniciar sesión
def loginPage(request):
    if request.method == "GET":
        return render(request, "signin.html", {
            "form": AuthenticationForm,
        })
    else:
        usuario = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if usuario is None:
            return render(request, "signin.html", {
                "form": AuthenticationForm,
                "error": "Error: El usuario o la contraseña son incorrectos."
            })
        else:
            login(request, usuario)
            return redirect("dashboard")

# Ver ganado.
def cattle(request):
    ganado = Ganado_Vacuno.objects.all()
    return render(request, "cattle.html", {
        "ganado": ganado
    })

# Registrar ganado.
def addCattle(request):
    if request.method == "GET":
        return render(request, "add_cattle.html", {
            "form": Ganado_Vacuno_Form
        })
    else:
        try:
            datos = Ganado_Vacuno_Form(request.POST)
            datos_Animal = datos.save(commit=False)
            datos_Animal.dueno = request.user
            datos_Animal.save()
            return redirect("cattle")
        except ValueError:
            return render(request, "add_cattle.html", {
                "form": Ganado_Vacuno_Form,
                "error": "Ingrese datos válidos por favor."
            })

# Editar datos del animal.
def cattleInfo(request, id):
    if request.method == "GET":
        animal = get_object_or_404(Ganado_Vacuno, pk=id)
        formulario = Ganado_Vacuno_Form(instance=animal)
        return render(request, "cattle_info.html", {"ganado": animal, "form": formulario})
    else:
        try:
            animal = get_object_or_404(Ganado_Vacuno, pk=id)
            formulario = Ganado_Vacuno_Form(request.POST, instance=animal)
            formulario.save()
            return redirect("cattle")
        except ValueError:
            return render(request, "cattle_info.html", {"ganado": animal, "form": formulario, "error": "Error al actualizar los datos del animal."})
        
# Eliminar a un animal de la BB. DD. del ganado.
def eraseCattle(request, id):
    animal = Ganado_Vacuno.objects.get(id = id)
    
    if request.method == "POST":
        animal.delete()
        return redirect("cattle")

# Estadísticas del ganado.
def statistics(request):
    return render(request, "statistics.html")

# API de gráfica de ganado por raza.
def graphRace(request):
    datos = []
    contadorRaza = {}
    raza = []

    ganado = Ganado_Vacuno.objects.all()

    for i in ganado:
        if i.dueno == request.user:
            
            if i.raza not in raza: 
                raza.append(i.raza)
                contadorRaza[i.raza] = 1
            else:
                contadorRaza[i.raza] += 1
    
    for x in raza:
        datos.append(contadorRaza[x])

    grafica = {
        "title": {
            "text": "Cantidad de animales según su raza"
        },
        "tooltip":{
            "show": True,
            "trigger": "axis",
            "triggerOn": "mousemove|click",
        },
        "xAxis": [
            {
                "type": "category",
                "data": raza,
            }
        ],
        "yAxis": [
            {
                "type": "value",
            }
        ],
        "series": [
            {
                "data": datos,
                "type": "bar",
                "itemStyle":{
                    "color": "#dc3545",
                },
                "showBackground": True,
                "backgroundStyle": {
                    "color": 'rgba(180, 180, 180, 0.2)'
                },
            }
        ],
    }

    return JsonResponse(grafica)

# API de gráfica de ganado por sexo.
def graphSex(request):
    datos = []
    contadorSexo = {}
    sexo = []
    colores = ["#1897ff", "#fe42a3"]

    ganado = Ganado_Vacuno.objects.all()

    for i in ganado:
        if i.dueno == request.user:
            
            if i.sexo not in sexo: 
                sexo.append(i.sexo)
                contadorSexo[i.sexo] = 1
            else:
                contadorSexo[i.sexo] += 1
    
    for x in sexo:
        datos.append(contadorSexo[x])

    grafica = {
        "title": {
            "text": "Cantidad de animales según su sexo",
            "left": "center",
        },
        "tooltip": {
            "trigger": "item",
        },
        "series": [
            {
                "color": colores,
                "name": "Sexo",
                "data": [
                    {"value": datos[0], "name": sexo[0]},
                    {"value": datos[1], "name": sexo[1]},
                    ],
                "type": "pie",
                "radius": "75%",
                "center": ["50%", "50%"],
                "emphasis": {
                    "itemStyle":{
                        "shadowBlur": 30,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)",
                    },
                }
            }
        ],
    }

    return JsonResponse(grafica)

# API de gráfica de ganado por peso por kilo.
def graphPriceByKg(request):
    datos = []
    arete = []

    ganado = Ganado_Vacuno.objects.all()

    for i in ganado:
        if i.dueno == request.user:
            arete.append(i.codigo_arete)
            datos.append(i.precio_por_kilo)

    grafica = {
        "title": {
            "text": "Animales según precio por kilogramo",
        },
        "tooltip":{
            "show": True,
            "trigger": "axis",
            "triggerOn": "mousemove|click",
        },
        "xAxis": {
            "type": "category",
            "data": arete,
        },
        "yAxis": {
            "type": "value",
        },
        "series": {
            "data": datos,
            "type": "line",
            "smooth": True
        },
    }

    return JsonResponse(grafica)