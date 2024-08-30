from django.urls import path
from .views import PostListCreateView, PostDetailView

urlpatterns = [
    # URL pattern for listing and creating posts
    # Maps the endpoint 'api/posts/' to the PostListCreateView view
    # The name 'post-list-create' is used to refer to this URL pattern in templates or reverse lookups
    path('api/posts/', PostListCreateView.as_view(), name='post-list-create'),

    # URL pattern for retrieving or updating a specific post based on its slug
    # Maps the endpoint 'api/posts/<slug:slug>/' to the PostDetailView view
    # '<slug:slug>' captures the slug parameter from the URL and passes it to the view
    # The name 'post-detail' is used to refer to this URL pattern in templates or reverse lookups
    path('api/posts/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
]
