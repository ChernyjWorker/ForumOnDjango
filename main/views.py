from typing import Any

from django.contrib import messages

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, FormMixin, DeleteView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy, reverse

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.shortcuts import get_object_or_404 

from .forms import CreatePostForm, CreateCommentaryForm
from .models import Category, Post, Commentary
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


class PostDetailView(FormMixin, DetailView):
    model = Post
    template_name = "main/post_detail.html"
    slug_field = 'slug'
    slug_url_kwarg = 'post_slug'
    form_class = CreateCommentaryForm
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    
    def form_valid(self, form):
        comment = form.save(commit=False)
        
        comment.post = self.object
        comment.user = self.request.user
        
        comment.save()
        
        messages.success(self.request, 'Коментарий успешно добавлен!')
        return super().form_valid(form)
    

    def get_success_url(self) -> str:
        return self.object.get_absolute_url()
    
            
    
    @navbar_preload
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['comment_form'] = self.get_form()
        context['commentaries'] = Commentary.objects.filter(post = self.object)
        return context
    

class CreatePost(LoginRequiredMixin, CreateView):
    template_name = 'main/post_create.html'
    form_class = CreatePostForm
    success_url = '/'
    
    @navbar_preload
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context
    
    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs['author'] = self.request.user
        return kwargs


class PostDeleteViews(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    template_name = 'main/post_delete.html'
    
    
    def test_func(self) -> bool | None:
        post = self.get_object()
        return self.request.user == post.author


class CommentDeleteViews(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Commentary
    template_name = 'main/comment_delete.html'
    
    
    def test_func(self) -> bool | None:
        comment = self.get_object()
        return self.request.user == comment.user
    
    
    def get_success_url(self) -> str:
        return reverse('post_detail', kwargs={'post_slug':self.object.post.slug})