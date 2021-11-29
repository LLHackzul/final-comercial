from django.urls import path
from . import views

urlpatterns = [
    path('paciente/', views.paciente_list, name='paciente_list'),
    path('agregar/paciente/', views.new_paciente, name='new_paciente'),
    path('paciente/<pk>/edit/', views.paciente_edit, name='paciente_edit'),
    path('paciente/<pk>/remove/', views.paciente_remove, name='paciente_remove'),

]