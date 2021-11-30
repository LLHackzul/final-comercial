from django.contrib import admin
from .models import Mantenimiento, Doctores, Pacientes, Anestesia, Assistant

admin.site.register(Doctores)
admin.site.register(Mantenimiento)
admin.site.register(Pacientes)
admin.site.register(Anestesia)
admin.site.register(Assistant)