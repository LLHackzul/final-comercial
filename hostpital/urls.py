from django.urls import path
from . import views

urlpatterns = [
    path('Assistant/', views.new_Assistant, name='new_Assistant'),
]