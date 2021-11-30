from django.urls import path
from . import views

urlpatterns = [
    path('doctor/', views.doctor_list, name='doctor_list'),
    path('agregar/doctor/', views.new_doctor, name='new_doctor'),
    path('doctor/<pk>/edit/', views.doctor_edit, name='doctor_edit'),
    path('doctor/<pk>/remove/', views.doctor_remove, name='doctor_remove'),
    path('mantenimiento/', views.mantenimiento_list, name='mantenimiento_list'),
    path('agregar/matenimiento/', views.new_mantenimiento, name='new_mantenimiento'),
    path('mantenimiento/<pk>/edit/', views.mantenimiento_edit, name='mantenimiento_edit'),
    path('mantenimiento/<pk>/remove/', views.mantenimiento_remove, name='mantenimiento_remove'),
]