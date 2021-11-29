from django.urls import path
from . import views

urlpatterns = [
    path('Assistant/', views.list_Assistant, name='list_Assistant'),
    path('agregar/Assistant', views.new_Assistant, name='new_Assistant'),
    path('Assistant/<pk>/edit/', views.edit_Assistant, name='edit_Assistant'),
    path('Assistant/<pk>/remove/', views.remove_Assistant, name='remove_Assistant'),
]