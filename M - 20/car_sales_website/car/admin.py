from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Car_Model)
admin.site.register(models.Comment)
admin.site.register(models.Order)