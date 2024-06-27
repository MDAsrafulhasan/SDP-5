from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
def home(request):
    return render(request, 'home.html')

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.userform(request.POST)
            if form.is_valid():
                messages.success(request,'Account was successfully signed up')
                form.save()
                # print(form.cleaned_data)
                # return redirect('profile')
        else:
            form = forms.userform()
        return render(request, 'signup.html' , {"form": form})
    else:
        return redirect('profile')

def userlogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request,user)
                    messages.success(request,"Logged in successfully")
                    return redirect('profile')
            
        else:
            form = AuthenticationForm()
        return render(request, 'login.html' , {"form": form})
    else:
        return redirect('profile')
    
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html',{'user': request.user})
    else:
        return redirect('login')

def userlogout(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('login')

def change_pass(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form = PasswordChangeForm(user = request.user,data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user = request.user)
        return render(request,'change_pass.html',{'form':form})
    else:
        return redirect('login')


def change_pass2(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form = SetPasswordForm(user = request.user,data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user = request.user)
        return render(request,'change_pass.html',{'form':form})
    else:
        return redirect('login')