from django.urls import path

from .views import RegisterView,CustomLoginView,CustomLogoutView, ProfileView


urlpatterns = [
    path('login/',CustomLoginView.as_view(), name='login'),
    path('logout/',CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>', ProfileView.as_view(),name='profile')
]
