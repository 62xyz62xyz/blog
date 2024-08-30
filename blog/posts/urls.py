from django.urls import path
from . import views

urlpatterns = [
    # URL pattern to list all posts
    # Maps to the 'posts' view function
    path('posts/', views.posts, name="posts"),

    # URL pattern to create a new post
    # Maps to the 'create' view function
    path('posts/new/', views.create, name="Create_Post"),

    # URL pattern to view details of a specific post
    # 'slug' is a URL parameter used to identify the post
    # Maps to the 'post_details' view function
    path('posts/<slug:slug>/', views.post_details, name="post_Details"),

    # URL pattern to edit a specific post
    # 'slug' is a URL parameter used to identify the post
    # Maps to the 'Edit' view function
    path('posts/<slug:slug>/edit/', views.Edit, name="Edit_Post"),

    # URL pattern to delete a specific post
    # 'slug' is a URL parameter used to identify the post
    # Maps to the 'Delete' view function
    path('posts/<slug:slug>/delete/', views.Delete, name="Delete_Post"),
]
