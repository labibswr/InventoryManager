from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.

# Registration Page
def register(request):
    # Verifying if there is a post request
    if request.method == 'POST':    
        form = CreateUserForm(request.POST)
        # Save if form input is valid
        if form.is_valid():
            form.save()
            uname = form.cleaned_data.get('username')
            messages.success(request, f'Profile for {uname} successfully created. Continue to login')
            return redirect('user-login')
    else:
        form = CreateUserForm()


    context = {
        'form':form,
        'page_name': 'register'
    }

    return render(request, 'UserPages/registration.html', context)

# Login page imported from authviews
class LoginPage(LoginView):
    template_name = 'UserPages/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'sign in'

        return context

# Logout page imported from authviews
class LogoutPage(LogoutView):
    template_name = 'UserPages/logout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'out'

        return context

# Profile management page
def profile(request):
    return render(request, 'UserPages/profile.html')

# Profile edit page
def edit(request):
    # Pulling the update forms created in forms.py
    if request.method =='POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        # Validity of the forms
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user-profile')

    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context={
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'UserPages/change_profile.html', context)