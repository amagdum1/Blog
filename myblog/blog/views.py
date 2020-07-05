from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post, Comment

from .forms import PostForm, CommentForm
from django.views.generic import (TemplateView, ListView, DetailView,
                                  CreateView, UpdateView,DeleteView)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from . import forms


from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
#view for signup

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("success")
    template_name = "registration/signup.html"

#after successful signup
class Success(TemplateView):
    template_name = 'blog/success.html'


#homepage
class HomeView(TemplateView):
    template_name = 'blog/index.html'

#about info
class AboutView(TemplateView):
    template_name = 'blog/about.html'

#list of all the posts
class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

#detailed view of post
class PostDetailView(DetailView):
    model = Post

#creating new post
class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

# editing post
class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post

#delete the post
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_draft_list.html'

    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')



#######################################
## Functions that require a pk match ##
#######################################

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})



