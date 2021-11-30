from django.db import models

class Assistant(models.Model):
    cui = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    secondName = models.CharField(max_length=100)
    firstSurname = models.CharField(max_length=100)
    secondSurname = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    AssistType = models.CharField(max_length=100)
    def __str__(self):
        return self.cui
class Anestesia(models.Model):
    cui = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    secondName = models.CharField(max_length=100)
    firstSurname = models.CharField(max_length=100)
    secondSurname = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    def _str_(self):
        return self.cui

class Pacientes(models.Model):
    historyNumber= models.CharField(max_length=100)
    firstName= models.CharField(max_length=100)
    secondName= models.CharField(max_length=100)
    firtSurname= models.CharField(max_length=100)
    secondSurname= models.CharField(max_length=100)
    age= models.CharField(max_length=100) 
    gender= models.CharField(max_length=100)

    def __str__(self):
        return self.historyNumber

class Doctores(models.Model):
    cui = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    secondName = models.CharField(max_length=100)
    firstSurname = models.CharField(max_length=100)
    secondSurname = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    def _str_(self):
        return self.cui
class Mantenimiento(models.Model):
    cui = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    secondName = models.CharField(max_length=100)
    firstSurname = models.CharField(max_length=100)
    secondSurname = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    def __str__(self):
        return self.cui
