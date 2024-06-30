from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_category(request):
    if request.method == 'POST':        # user post request korse
        category_form = forms.CategoryForm(request.POST) # user er post request er data ekhane rakhsi
        if category_form.is_valid():
            category_form.save()
            return redirect('add_category')
    else:
        category_form = forms.CategoryForm()
    return render(request , 'add_category.html',{'form':category_form})