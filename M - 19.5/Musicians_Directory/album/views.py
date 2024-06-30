from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import forms
from . import models

# using Function based view:
# def AlbumViews(request):
#     # albumform = forms.AlbunForm()
#     # return render(request, 'album.html', {'album_form': albumform})
#     if request.method=='POST':
#         albumform = forms.AlbunForm(request.POST)
#         if albumform.is_valid():
#             albumform.save()
#             # return redirect('album_page')
#             return redirect('table_page')
#     else:
#         albumform = forms.AlbunForm()
#     return render(request,'album.html',{'album_form':albumform})


# def EditAlbumViews(request,id):
#     albumid = models.AlbumModel.objects.get(pk=id)
#     albumform = forms.AlbunForm(instance=albumid)
#     if request.method=='POST':
#         albumform = forms.AlbunForm(request.POST,instance=albumid)
#         if albumform.is_valid():
#             albumform.save()
#             return redirect('table_page')

#     return render(request,'album.html',{'album_form':albumform})


# def Delete_Album(request,id):
#     albumid = models.AlbumModel.objects.get(pk=id)
#     albumid.delete()
#     return redirect('table_page')





#using class based view:


from django.contrib import messages
from . import forms
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class ClassView_UserRegister(CreateView):
    template_name = 'register.html'
    form_class = forms.UserRegister
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        messages.success(self.request , "Account created successfully")
        return super().form_valid(form)
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Register'
        return context
    

class ClassView_UserLogin(LoginView):
    template_name = 'register.html'
    def get_success_url(self):
        return reverse_lazy('album_page')
    def form_valid(self, form):
        messages.success(self.request, "Looged in successfully")
        return super().form_valid(form)
    
    def form_invalid(self,form) :
        messages.error(self.request, "Invalid username or password")
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    
@method_decorator(login_required,name="dispatch")
class ClassView_UserLogout(LoginRequiredMixin,LogoutView):
    next_page = reverse_lazy('home_page')
    login_url = reverse_lazy('home_page')

    # def get_context_data(self, **kwargs):
    #     messages.success(self.request , "logged out successfully")
    #     return super().get_context_data(**kwargs)

@method_decorator(login_required,name="dispatch")
class ClassView_AlbumViews(LoginRequiredMixin,CreateView):
    model = models.AlbumModel
    form_class = forms.AlbunForm
    template_name = 'album.html'
    success_url = reverse_lazy('table_page')
    login_url = reverse_lazy('home_page')

@method_decorator(login_required,name="dispatch")
class ClassView_EditAlbumViews(LoginRequiredMixin,UpdateView):
    model = models.AlbumModel
    form_class = forms.AlbunForm
    pk_url_kwarg = 'id'
    template_name = 'album.html'
    success_url = reverse_lazy('table_page')
    login_url = reverse_lazy('home_page')

@method_decorator(login_required,name="dispatch")
class ClassView_Delete(LoginRequiredMixin,DeleteView):
    model = models.AlbumModel
    pk_url_kwarg = 'id'
    template_name = 'delete.html'
    success_url = reverse_lazy('table_page')
    login_url = reverse_lazy('home_page')