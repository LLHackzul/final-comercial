from django.urls import path
from . import views

urlpatterns = [
    path('doctor/', views.doctor_list, name='doctor_list'),
    path('agregar/doctor/', views.new_doctor, name='new_doctor'),
    path('doctor/<pk>/edit/', views.doctor_edit, name='doctor_edit'),
    path('doctor/<pk>/remove/', views.doctor_remove, name='doctor_remove'),
]