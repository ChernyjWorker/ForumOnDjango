from django.shortcuts import render

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