from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from . models import Character

# Create your views here. 
def home(request):
    """
    Renders the home page.
    
    Args:
        request: The Http request object.
        
    Returns: 
        HttpResponse: Rendered 'home.html' template.
    """ 
    return render(request, 'home.html')


def register_new_user(request):
    """
    Handles user registration.
    
    if the request method is POST, ot validates the user registration form.
    If valid, it saves the new user and redirects to the login page.
    Otherwise, it displays the registration form.
    
    Args: 
        request: The HTTP request object.
        
    Returns: 
        HttpResponse: Rendered 'registration/register.html' template with the form.
        Redirect: Redirects to the login page upon successful registration.
    """
    
    if request.POST:
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('login')
        
    form = UserCreationForm()
    return render(request, 'registration/register.html', {'form':form})

@login_required
def characters(request):
    """
    Displays a list of characters fro authenticted users.
    
    Fetches all Character objects from the database.
    If none exist, returns 404 error page.
    
    Args:
        requset: The HTTP request object.
        
    Returns:
        HttpResponse: Rendered 'characters.html' template with a list of characters.
    """
    list_of_characters = get_list_or_404(Character)
    return render(request, 'characters.html', {'characters':list_of_characters})


@login_required
def about(request):
    """
    Renders the about page for authenticated users.
    
    Args:
        request: The HTTP request object.
        
    Returns: 
        HttpResponse: Rendered 'about.html' template.
    """
    return render(request, 'about.html')

