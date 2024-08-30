"""
URL configuration for the blog project.

The `urlpatterns` list routes URLs to views. For more information, please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/

Examples:
Function views:
    1. Add an import: from my_app import views
    2. Add a URL to urlpatterns: path('', views.home, name='home')

Class-based views:
    1. Add an import: from other_app.views import Home
    2. Add a URL to urlpatterns: path('', Home.as_view(), name='home')

Including another URLconf:
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns: path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # Admin site URL pattern
    # Maps the endpoint 'admin/' to Django's admin site
    path('admin/', admin.site.urls),

    # Home page URL pattern
    # Maps the root endpoint '' to the Home view function in views
    path('', views.Home, name='Home'),

    # User signup URL pattern
    # Maps the endpoint 'signup' to the signup view function in views
    path('signup/', views.signup, name='signup'),

    # User login URL pattern
    # Maps the endpoint 'login' to the login view function in views
    path('login', views.login, name='login'),

    # Includes URL patterns from the 'api' app
    # Any URL starting with '' will be matched to the URL patterns defined in 'api.urls'
    path('', include('api.urls')),

    # Includes URL patterns from the 'posts' app
    # Any URL starting with '' will be matched to the URL patterns defined in 'posts.urls'
    path('', include('posts.urls')),

    # Custom task URL pattern
    # Maps the endpoint 'perform-task/' to the perform_task view function in views
    path('perform-task/', views.perform_task, name='perform_task'),
]
