from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('characters/', views.characters, name='characters'),
    path('about/', views.about, name='about'),
    
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register_new_user, name='register'),
]
