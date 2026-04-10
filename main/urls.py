from django.urls import path

from .views import PostListView, post_detail, CreatePost

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('new/', CreatePost.as_view(), name='post_new'),
    path('/<str:post_slug>', post_detail, name='post_detail'),
]
