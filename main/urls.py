from django.urls import path

from .views import post_list, post_detail, CreatePost

urlpatterns = [
    path('', post_list, name='post_list'),
    path('new/', CreatePost.as_view(), name='post_new'),
    path('/<str:post_slug>', post_detail, name='post_detail'),
]
