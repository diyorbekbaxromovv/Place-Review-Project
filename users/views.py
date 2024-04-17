from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import RegisterForm, LoginForm, ProfileUpdateForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy





class RegisterView(View):
    def get(self, request):
        form = RegisterForm
        return render(request, 'users/register.html', context={'form': form})
    
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('user:login')
        
        return render(request, 'users/register.html', context={'form': form})
    
    
class LoginView(View):
    def get(self, request): 
        form = LoginForm()
        
        return render(request, 'users/login.html', context={'form': form})
    
    
    def post(self, request):
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('food:index')
        
        return render(request, 'users/login.html', context={'form': form})  
    
    
class CustomPasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'users/reset_password.html'
    success_url = reverse_lazy('food:index')

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('users:login')


class ProfileUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        form = ProfileUpdateForm(instance=request.user)
        return render(request, 'users/profile.html', context={'form': form})
    
    def post(self, request):
        profile_update_form  = ProfileUpdateForm(instance=request.user, data=request.POST)
        
        if profile_update_form.is_valid():
            profile_update_form.save()
            return redirect('food:index')
        
        return render(request, 'users/profile.html', context={'form': profile_update_form})
    
    
class ProfileView(View):
    def get(self, request):
        
        return render(request, 'users/profile_new.html')