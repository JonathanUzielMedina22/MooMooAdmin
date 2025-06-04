from django.contrib import admin
from .models import Ganado_Vacuno

class Ganado_Admin(admin.ModelAdmin):
    readonly_fields = ("agregado", )

# Register your models here.
admin.site.register(Ganado_Vacuno, Ganado_Admin)