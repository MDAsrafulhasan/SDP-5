from django import forms
from . import models
class Brand_Form(forms.ModelForm):
    class Meta:
        model = models.Brand_Model
        fields = '__all__'