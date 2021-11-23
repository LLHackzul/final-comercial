from django.urls import path
from . import views

urlpatterns = [
    path('anestesia/', views.new_anestesia, name='new_anestesia'),
]