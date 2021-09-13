from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from .models import ContactUs, CustomUser
from .forms import CustomUserCreationForm, ContactUsForm
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout


def signupView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = CustomUser.objects.get(username=username)
            customer_group = Group.objects.get(name='Customer')
            customer_group.user_set.add(signup_user)
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form':form})

def signinView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('shop:allProductCategories')
            else:
                return redirect('accounts:signup')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form':form})
    
def signoutView(request):
    logout(request)
    return redirect('accounts:signin')

def contactUs(request):
    if request.method == 'POST':
        f = ContactUsForm(request.POST)
        if f.is_valid():
            f.save()
            messages.add_message(request, messages.INFO, 'Your form was submitted. We will get back to you as soon as possible. Have a good HAIR day!')
            return redirect('accounts:contactUs')
    else:
        f = ContactUsForm()
    return render(request, 'contactUs.html', {'form': f})