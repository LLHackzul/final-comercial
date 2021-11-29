from django.urls import path
from . import views

urlpatterns = [
    path('anestesia/', views.anestesia_list, name='anestesia_list'),
    path('agregar/anestesia/', views.new_anestesia, name='new_anestesia'),
    path('anestesia/<pk>/edit/', views.anestesia_edit, name='anestesia_edit'),
    path('anestesia/<pk>/remove/', views.anestesia_remove, name='anestesia_remove'),
]