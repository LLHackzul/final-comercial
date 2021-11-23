from django.urls import path
from . import views

urlpatterns = [
    path('mantenimiento/', views.new_mantenimiento, name='new_mantenimiento'),
]