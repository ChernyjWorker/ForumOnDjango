from typing import Any

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView


from .decorators import navbar_preload

from django.utils.text import slugify

from .forms import CreatePostForm
from .models import Post


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

def post_detail(request, post_slug):
    template = 'main/post_detail.html'
    
    post = Post.objects.get(slug=post_slug)
    
    context = {
        'post' : post
    }
    
    return render(request, template, context)


class CreatePost(CreateView):
    template_name = 'main/post_create.html'
    form_class = CreatePostForm
    success_url = '/'
    
    @navbar_preload
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context
    