from django.db import models
from musician.models import MusicianModel
from django.core.validators import *

# Create your models here.
class AlbumModel(models.Model):
    Album_name = models.CharField(max_length=100)
    musicians = models.ForeignKey(MusicianModel,on_delete=models.CASCADE)
    Album_release_date = models.DateField(auto_now_add=True)
    # rating = models.IntegerField(validators=[MinValueValidator(1),MaxLengthValidator(5)],help_text="Please submit a rating between 1 to 5")
    rating = models.CharField(max_length=1 , help_text="please submit a rating between 1 to 5")

    
    def __str__(self):
        return f"{self.Album_name} - {self.musicians.First_Name}"
