from django.shortcuts import render
from car.models import Car_Model
from brand.models import Brand_Model
from django.views.generic import DetailView
def home(request , brand_slug=None):
    data = Car_Model.objects.all()
    if brand_slug is not None:
        brand = Brand_Model.objects.get(slug=brand_slug)
        data = Car_Model.objects.filter(brand=brand)
    brand = Brand_Model.objects.all()
    return render(request, 'home.html',{'data':data , 'brand':brand})

# def car_details(request,id):
#     data = Car_Model.objects.get(pk=id)
#     return render(request, 'car_details.html', {'data': data})

