from django.db import models
from phonenumber_field import *
# Create your models here.
class MusicianModel(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Phone_number = models.CharField(max_length=12)
    Instrument_Type = models.CharField(max_length=100)

    def __str__(self):
        return self.First_Name