from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic import DetailView
from . import forms
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .import models
from django.contrib.auth.forms import UserChangeForm

# Create your views here.
def car(request):
    return render(request, 'car.html')

# @login_required
# def profile(request):
#     return render(request, 'profile.html')


def buy_car(request, id):
    car = models.Car_Model.objects.get(pk=id)
    
    if request.method == 'POST':
        if car.quantity > 0:
            car.quantity -= 1
            car.save()
            models.Order.objects.create(user=request.user, car=car)
            messages.success(request, "You have successfully purchased")
            # return redirect('car_details')
            # return render(request, 'car_details.html', {'car': car})
            return redirect('car_details' , id)
        else:
            messages.error(request, "Sorry car is out of stock.")
            return redirect('car_details' , id)


@method_decorator(login_required, name='dispatch')
class ClassView_Profile(LoginRequiredMixin,View):
    template_name = 'profile.html'
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        orders = models.Order.objects.filter(user=request.user)
        return render(request, self.template_name,{'orders': orders})


class ClassView_Signup(CreateView):
    form_class = forms.SignupForm
    template_name = 'signup.html'
    success_url = reverse_lazy('profile')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        return super().dispatch(request, *args, **kwargs)
    

    def form_valid(self, form):
        messages.success(self.request , "Account created successfully")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Signup' 
        return context
    
class ClassView_Login(LoginView):
    template_name = 'signup.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, "Login successful")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password")
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

# @method_decorator(login_required, name='dispatch')
# class ClassView_Logout(LoginRequiredMixin,LogoutView):
#     next_page = reverse_lazy('homepage')
#     login_url = reverse_lazy('login')

class ClassView_UpdateProfile(UpdateView):
    form_class = forms.EditUserForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self) :
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "Profile updated successfully")
        return super().form_valid(form)
    
class ClassView_CarDetails(DetailView):
    model = models.Car_Model
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data= self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        # if self.request.method == 'POST':
        #     comment_form = forms.CommentForm(data= self.request.POST)
        #     if comment_form.is_valid():
        #         new_comment = comment_form.save(commit=False)
        #         new_comment.car = car
        #         new_comment.save()
        # else:
        comment_form = forms.CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    