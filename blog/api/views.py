from rest_framework import generics, viewsets, serializers
from .models import Post
from .serializers import PostSerializer, PostDetailsSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class PostListCreateView(generics.ListCreateAPIView):
    """
    View for listing all posts and creating a new post.
    """
    # Queryset to use for this view; includes all Post objects
    queryset = Post.objects.all()
    
    # Serializer class to use for serializing the Post objects
    serializer_class = PostSerializer
    
    # Permissions: Allows authenticated users to create posts; unauthenticated users can only view the list
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """
        Override the default behavior to automatically set the author to the current user
        when creating a new post.
        """
        serializer.save(author=self.request.user)

class PostDetailView(generics.RetrieveAPIView):
    """
    View for retrieving a specific post by its slug.
    """
    # Serializer class to use for serializing the detailed view of a single Post object
    serializer_class = PostDetailsSerializer
    
    # Field to use for looking up a specific post; slug in this case
    lookup_field = 'slug'

    def get_queryset(self):
        """
        Override the default queryset to filter posts by the slug provided in the URL.
        """
        # Filter the queryset to include only the post with the given slug
        return Post.objects.filter(slug=self.kwargs['slug'])
