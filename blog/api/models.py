from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Post(models.Model):
    # Title of the post with a maximum length of 200 characters, must be unique
    title = models.CharField(max_length=200, unique=True)
    
    # URL-friendly version of the title for use in URLs; can be blank but must be unique
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    
    # Main content of the post
    content = models.TextField()
    
    # Author of the post; linked to Django's User model; if the user is deleted, all their posts are also deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Timestamp when the post was created; automatically set when the post is first created
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Timestamp when the post was last updated; automatically updated whenever the post is saved
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Automatically generate the slug from the title if it's not provided
        if not self.slug:
            self.slug = slugify(self.title)
        # Call the parent class's save method to ensure the post is saved to the database
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        # String representation of the post, used in the Django admin interface and other places
        return self.title
