from django.urls import path
from . import views

urlpatterns = [
    path('mantenimiento/', views.mantenimiento_list, name='mantenimiento_list'),
    path('agregar/matenimiento/', views.new_mantenimiento, name='new_mantenimiento'),
    path('mantenimiento/<pk>/edit/', views.mantenimiento_edit, name='mantenimiento_edit'),
    path('mantenimiento/<pk>/remove/', views.mantenimiento_remove, name='mantenimiento_remove'),
]