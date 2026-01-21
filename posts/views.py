from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
)
from .models import Post

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

class PostDetailView(DetailView): # GET Method
    """
    PostDetailView is going to retriece a single element from the Post table in the db.
    """
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "single_post"