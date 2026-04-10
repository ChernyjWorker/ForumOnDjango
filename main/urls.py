from django.urls import path

from .views import PostListView, PostFilterListView, PostDetailView, CreatePost

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<slug:category_slug>', PostFilterListView.as_view(), name='post_filter'),
    path('new/', CreatePost.as_view(), name='post_new'),
    path('<slug:post_slug>/', PostDetailView.as_view(), name='post_detail'),
]
