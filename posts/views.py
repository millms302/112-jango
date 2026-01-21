from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post, Status
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.

class PostListView(ListView):
    """
    PostListView is going to retrieve all of the objexts from the Post table in db
    """

    # template_name attribute is going to render a specific HTML file
    template_name = "posts/list.html"
    # model is going to be from which table we want to retrieve the data
    model = Post
    # context_object_name allows us to modifyt the name on how we call it in the HTMLS
    context_object_name = "posts"
    published_status = Status.objects.get(name="Published")
    # Queryset attribute allows us to select some data from the db by using the model class.
    queryset = Post.objects.filter(status=published_status).order_by("created_on").reverse()

class PostDetailView(DetailView): # GET Method
    """
    PostDetailView is going to retrieve a single element from the Post table in the db.
    """
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "single_post"

class PostCreateView(CreateView):
    """
    PostCreateView is going to create new posts
    """
    template_name = "posts/new.html"
    model=Post
    fields=["title", "subtitle", "body"]

    def form_valid(self, form):
        print(User.objects.all())
        form.instance.author = User.objects.last()
        return super().form_valid(form)
    
class PostUpdateView(UpdateView):
    """
    PostUpdateView allows us to edit posts.
    """
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "body"]

class PostDeleteView(DeleteView):
    """
    PostDeleteView allows us to delete posts.
    """
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("post_list")