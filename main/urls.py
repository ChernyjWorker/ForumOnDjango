from django.urls import path

from .views import (PostListView, PostFilterListView, PostDetailView, CreatePost, 
                    PostDeleteViews, CommentDeleteViews)


urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<slug:category_slug>', PostFilterListView.as_view(), name='post_filter'),
    path('new/', CreatePost.as_view(), name='post_new'),
    path('delpost/<int:pk>', PostDeleteViews.as_view(), name='post_delete'),
    path('delcomm/<int:pk>', CommentDeleteViews.as_view(), name='comment_delete'),
    path('<slug:post_slug>/', PostDetailView.as_view(), name='post_detail'),
]
