from django.shortcuts import render,redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def add_post(request):
    if request.method == 'POST':      # user post request korse 
        post_form = forms.PostForm(request.POST)      #  user er post request er data ekhane rakhsi
        if post_form.is_valid():
            post_form.instance.author = request.user   # add post er jonno ekhn id'r malik fixed kora hoise.age select kora lagto ,ekhn zar id tar post hobe (malik fixed)
            post_form.save()
            return redirect('add_post')
    else:
        post_form = forms.PostForm()
    return render(request , 'add_post.html',{'form':post_form})

@login_required
def edit_post(request,id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)

    print(post.title)
    if request.method == 'POST':      # user post request korse 
        post_form = forms.PostForm(request.POST, instance=post)      #  user er post request er data ekhane rakhsi
        if post_form.is_valid():
            post_form.instance.author = request.user   # add post er jonno ekhn id'r malik fixed kora hoise.age select kora lagto ,ekhn zar id tar post hobe (malik fixed)
            post_form.save()
            return redirect('homepage')
    # else:
    #     post_form = forms.PostForm()
    return render(request , 'add_post.html',{'form':post_form})

@login_required
def delete_post(request,id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')