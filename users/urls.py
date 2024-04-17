from django.urls import path
from . import views
from .views import LoginView, LogoutView, RegisterView, CustomPasswordChangeView
from django.contrib.auth import views as auth_views
app_name = 'users'


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileUpdateView.as_view(), name='profile'),
    path('profile_new/', views.ProfileView.as_view(), name='profile_new'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    
    path('api/login/', LoginView.as_view(), name='api-login'),
    path('api/logout/', LogoutView.as_view(), name='api-logout'),
    
]
