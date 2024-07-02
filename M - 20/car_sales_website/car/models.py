from django.db import models
from brand.models import Brand_Model
from django.contrib.auth.models import User
# Create your models here.


class Car_Model(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand_Model, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='./car./media./uploads./')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    car = models.ForeignKey(Car_Model, on_delete=models.CASCADE,related_name='comments')
    user = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user}'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car_Model, on_delete=models.CASCADE)