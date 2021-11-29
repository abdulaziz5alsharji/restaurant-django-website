from django.db import models

# Create your models here.

class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    number_of_person = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    
    def __str__(self) -> str:
        return self.name