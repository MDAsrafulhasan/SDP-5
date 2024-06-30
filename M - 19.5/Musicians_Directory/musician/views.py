from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
# def MusicianView(request):
#     # musician_form = forms.MusicianForm()
#     # return render(request,'musician.html',{'musician_form':musician_form})
#     if request.method == 'POST':
#         musician_form = forms.MusicianForm(request.POST)
#         if musician_form.is_valid():
#             musician_form.save()
#             # return redirect('musician_page')
#             return redirect('table_page')
        
#     else:
#         musician_form = forms.MusicianForm()
#     return render(request,'musician.html',{'musician_form':musician_form})


# def EditMusicianView(request,id):
#     musician_id = models.MusicianModel.objects.get(pk=id)
#     musician_form = forms.MusicianForm(instance=musician_id)
#     if request.method == 'POST':
#         musician_form = forms.MusicianForm(request.POST, instance=musician_id)
#         if musician_form.is_valid():
#             musician_form.save()
#             return redirect('table_page')

#     return render(request,'musician.html',{'musician_form':musician_form})






# using class bassed view
from django.views.generic import CreateView,UpdateView
from . import models
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

@method_decorator(login_required , name = "dispatch")
class ClassView_MusicianCreate(LoginRequiredMixin,CreateView):
    model = models.MusicianModel
    form_class = forms.MusicianForm
    template_name = 'musician.html'
    success_url = reverse_lazy('musician_page')
    login_url = reverse_lazy('home_page')

@method_decorator(login_required,name = "dispatch")
class ClassView_EditMusicianView(LoginRequiredMixin,UpdateView):
    model = models.MusicianModel
    form_class = forms.MusicianForm
    pk_url_kwarg = 'id'
    template_name = 'musician.html'
    success_url = reverse_lazy('table_page')
    login_url = reverse_lazy('home_page')
