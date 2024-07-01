from django.shortcuts import render
from django.views.generic.edit import CreateView
from . import forms
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def car(request):
    return render(request, 'car.html')

@login_required
def profile(request):
    return render(request, 'profile.html')


# @method_decorator(login_required, name='dispatch')
# class ClassView_Profile(LoginRequiredMixin):
#     template_name = 'homepage.html'
#     login_url = reverse_lazy('profile')


class ClassView_Signup(CreateView):
    form_class = forms.SignupForm
    template_name = 'signup.html'
    success_url = reverse_lazy('profile')
    

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

@method_decorator(login_required, name='dispatch')
class ClassView_Logout(LoginRequiredMixin,LogoutView):
    next_page = reverse_lazy('homepage')
    login_url = reverse_lazy('homepage')