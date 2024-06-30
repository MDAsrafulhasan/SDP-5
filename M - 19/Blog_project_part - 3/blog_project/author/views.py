from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,update_session_auth_hash,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy


# Create your views here.
# def add_author(request):
#     if request.method == 'POST':      # user post request korse 
#         author_form = forms.AuthorForm(request.POST)      #  user er post request er data ekhane rakhsi
#         if author_form.is_valid():
#             author_form.save()
#             return redirect('add_author')
#     else:
#         author_form = forms.AuthorForm()
#     return render(request , 'add_author.html',{'form':author_form})




def register(request):
    if request.method == 'POST':      # user post request korse 
        register_form = forms.RegisterForm(request.POST)      #  user er post request er data ekhane rakhsi
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "Account created successfully")
            return redirect('register')
    else:
        register_form = forms.RegisterForm()
    return render(request , 'register.html',{'form':register_form , 'type':'Register'})


def user_login(request):
    if request.method == 'POST':      # user post request korse 
        form = AuthenticationForm(request , request.POST)      #  user er post request er data ekhane rakhsi
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username = user_name, password =  user_pass)
            if user is not None :
                messages.success(request, "Login successfully")
                login(request , user)
                return redirect('profile')
            else:
                messages.warning(request, "Login information is incorrect")
                return redirect('register')
    else:
        form = AuthenticationForm()
    return render(request , 'register.html',{'form':form , 'type':'Login'})

# using class view:
class ClassView_UserLogin(LoginView):
    template_name = 'register.html'
    # success_url = reverse_lazy('profile')
    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request,"Logged in successfully")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request,"Logged in information incorrect")
        return super().form_invalid(form)
    
    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
        
    
    

@login_required
def profile(request):
    data = Post.objects.filter(author = request.user)
    return render(request , 'profile.html',{'data':data , 'user':request.user})


@login_required
def edit_profile(request):
    if request.method == 'POST':      # user post request korse 
        profile_form = forms.ChangeUserForm(request.POST , instance = request.user)      #  user er post request er data ekhane rakhsi
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Profile updated successfully")
            return redirect('profile')
    else:
        profile_form = forms.ChangeUserForm(instance = request.user)
    return render(request , 'update_profile.html',{'form':profile_form})


def pass_change(request):
    if request.method == 'POST':      # user post request korse 
        form = PasswordChangeForm(request.user,data = request.POST)      #  user er post request er data ekhane rakhsi
        if form.is_valid():
            form.save()
            messages.success(request, "Password updated successfully")
            update_session_auth_hash(request , form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user = request.user)
    return render(request , 'pass_change.html',{'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('user_login')
