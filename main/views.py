from typing import Any

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from django.shortcuts import get_object_or_404 

from .forms import CreatePostForm
from .models import Category, Post
from decorators import navbar_preload


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "main/post_list.html"
    context_object_name = 'posts'
    
    def get_queryset(self):
        return Post.objects.all()
    
    @navbar_preload
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostFilterListView(ListView):
    model = Post
    template_name = "main/post_list.html"
    context_object_name = 'posts'
    
    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['category_slug'])
        return Post.objects.filter(category = category)
    
    @navbar_preload
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "main/post_detail.html"
    slug_field = 'slug'
    slug_url_kwarg = 'post_slug'
    
    @navbar_preload
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
    



class CreatePost(CreateView):
    template_name = 'main/post_create.html'
    form_class = CreatePostForm
    success_url = '/'
    
    @navbar_preload
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context
    