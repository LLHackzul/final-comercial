from django.contrib import admin
from .models import Mantenimiento, Doctores
# Register your models here.
admin.site.register(Doctores)
admin.site.register(Mantenimiento)
