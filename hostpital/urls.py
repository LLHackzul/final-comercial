from django.urls import path
from . import views

urlpatterns = [
    path('doctor/', views.new_doctor, name='new_doctor'),
]