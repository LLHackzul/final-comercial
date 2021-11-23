from django.db import models

# Create your models here.
class Doctores(models.Model):
    cui = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    secondName = models.CharField(max_length=100)
    firstSurname = models.CharField(max_length=100)
    secondSurname = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    def __str__(self):
        return self.cui