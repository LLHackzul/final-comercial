from django.db import models

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