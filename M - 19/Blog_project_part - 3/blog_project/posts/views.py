from django.shortcuts import render,redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
# for class view:
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

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

#using class view:
@method_decorator(login_required,name="dispatch")
class ClassViewAddPost(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)





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

# using class view:
@method_decorator(login_required,name="dispatch")
class ClassViewEditPost(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    pk_url_kwarg = 'id'
    template_name = 'add_post.html'
    success_url = reverse_lazy('homepage')





@login_required
def delete_post(request,id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')

# using class view:
@method_decorator(login_required,name="dispatch")
class ClassViewDeletePost(DeleteView):
    model = models.Post
    pk_url_kwarg = 'id'
    template_name = 'delete.html'
    success_url = reverse_lazy('homepage')


class ClassView_DetailsView(DetailView):
    model = models.Post
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'

    def post(self, *args, **kwargs):
        comment_form = forms.CommentForm(data = self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(self, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = forms.CommentForm()

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

                
