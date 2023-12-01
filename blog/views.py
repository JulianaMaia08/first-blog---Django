from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, TemplateView
from django.utils import timezone
from .models import Post
from .forms import PostForm
# Create your views here.

class PostList(ListView):
    template_name = "post_list.html"
    model = Post

class PostDetail(DetailView):
    template_name = "post_detail.html"
    model = Post

class ThanksPostView(TemplateView):
    template_name = 'thanks_post.html'

class NewPost(FormView):
    form_class = PostForm
    template_name = "post_edit.html"


    def form_valid(self, form):
        # O formulário é válido, faça algo com os dados
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return redirect('blog:post_detail', pk=post.pk)

        return super().form_valid(form)

