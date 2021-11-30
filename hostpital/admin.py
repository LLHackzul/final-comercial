from django.contrib import admin

from .models import Mantenimiento, Doctores, Pacientes

admin.site.register(Doctores)
admin.site.register(Mantenimiento)
admin.site.register(Pacientes)