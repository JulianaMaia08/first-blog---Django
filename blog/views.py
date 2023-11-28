from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import Post
# Create your views here.

class PostList(ListView):
    template_name = "post_list.html"
    model = Post

class PostDetail(DetailView):
    template_name = "post_detail.html"
    model = Post
