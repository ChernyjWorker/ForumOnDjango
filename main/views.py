from typing import Any

from django.shortcuts import render
from django.views.generic.edit import CreateView

from django.utils.text import slugify

from .forms import CreatePostForm
from .models import Post
# Create your views here.

def post_list(request):
    template = 'main/post_list.html'
    posts = Post.objects.order_by('-created_at')
    context = {
        'posts' : posts
    }
    
    return render(request, template, context)


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
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context
    