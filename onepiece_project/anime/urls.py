from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

# URL patterns for the Django application
urlpatterns = [
    path('', views.home, name='home'),
    # Maps the root URL ('') to the `home` view. This is the default landing page of the application.

    path('characters/', views.characters, name='characters'),
    # Maps the 'characters/' URL to the `characters` view.
    # Requires user authentication to access. Displays a list of characters.

    path('about/', views.about, name='about'),
    # Maps the 'about/' URL to the `about` view.
    # Requires user authentication to access. Displays the about page.

    path('login/', LoginView.as_view(), name='login'),
    # Maps the 'login/' URL to the default Django login view.
    # Handles user login using Django's built-in authentication system.

    path('logout/', LogoutView.as_view(), name='logout'),
    # Maps the 'logout/' URL to the default Django logout view.
    # Logs the user out and redirects to the login page or another default URL.

    path('register/', views.register_new_user, name='register'),
    # Maps the 'register/' URL to the `register_new_user` view.
    # Handles user registration and displays a form for creating new user accounts.
]
