from django.shortcuts import render
from album.models import AlbumModel
# def home(request):
#     datas = AlbumModel.objects.all()
#     return render(request, 'table.html', {'datas':datas})



# using class based view

from django.views.generic import ListView

class ClassView_Home(ListView):
    model = AlbumModel
    template_name = 'table.html'
    context_object_name = 'datas'

class ClassView_Table(ListView):
    model = AlbumModel
    template_name = 'table.html'
    context_object_name = 'datas'