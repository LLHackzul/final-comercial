from django.urls import path
from . import views

urlpatterns = [
    path('paciente/', views.new_paciente, name='new_paciente'),
]