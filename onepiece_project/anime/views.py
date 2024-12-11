from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from . models import Character

# Create your views here. 
def home(request): 
    return render(request, 'home.html')


def register_new_user(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('login')
        
    form = UserCreationForm()
    return render(request, 'registration/register.html', {'form':form})

@login_required
def characters(request):
    list_of_characters = get_list_or_404(Character)
    return render(request, 'characters.html', {'characters':list_of_characters})


@login_required
def about(request):
    return render(request, 'about.html')

