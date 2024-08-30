from django.shortcuts import render
from api.models import Post
from django.http import HttpResponse
from django.core.paginator import Paginator
from .forms import PostForm

# Create your views here.

def posts(request):
    # Retrieve all Post objects, ordered by creation date
    post_list = Post.objects.all().order_by('created_at')
    
    # Paginate the post list, 9 posts per page
    paginator = Paginator(post_list, 9)
    # Get the current page number from the query parameters
    page_number = request.GET.get('page')
    # Get the page object for the current page
    page_obj = paginator.get_page(page_number)
    
    # Truncate the content of each post to the first 200 characters for preview
    for x in post_list:
        x.content = x.content[:200]
    
    # Render the 'posts.html' template with the paginated post list
    return render(request, 'posts.html', {'page': page_obj, 'post': post_list})

def post_details(request, slug):
    # Retrieve the post with the given slug
    post_detail = Post.objects.get(slug=slug)
    
    # Render the 'post_details.html' template with the post detail
    return render(request, 'post_details.html', {'post': post_detail})

def create(request):
    # Handle GET request to display the post creation form
    if request.method == 'GET':
        # Initialize an empty post dictionary for the form
        post = {'title': None, 'slug': None, 'content': None}
        
        # Render the 'NewPost.html' template with the form
        return render(request, 'NewPost.html', {
            'post': post,
            'target': 'Submit',
            'method': 'POST',
            'action': '/posts/new/'
        })
    
    # Handle POST request to create a new post
    elif request.method == 'POST' and request.user.username:
        # Get the post details from the form data
        slug = request.POST.get('slug')
        content = request.POST.get('content')
        title = request.POST.get('title')
        author = request.user
        
        # Check if a post with the same title or slug already exists
        if len(Post.objects.filter(title=title)) == 0 and len(Post.objects.filter(slug=slug)) == 0:
            # Create and save the new post
            post = Post(title=title, slug=slug, content=content, author=author)
            post.save()
            
            # Return a success response
            return HttpResponse("Done GO HOME <a href='/'>HOME</a>")
        else:
            # Return an error response if title or slug already exists
            return HttpResponse("Title or Slug Exists")
    
    # Return an error response if the user is not logged in
    else:
        return HttpResponse("You are not logged in")

def Edit(request, slug):
    # Retrieve the post with the given slug
    record = Post.objects.get(slug=slug)
    
    # Handle GET request to display the post edit form
    if request.method == 'GET':
        # Render the 'NewPost.html' template with the post data for editing
        return render(request, 'NewPost.html', {
            'post': record,
            'target': 'Update',
            'method': 'POST',
            'action': '/posts/' + slug + '/edit/'
        })
    
    # Handle POST request to update the post
    elif request.method == 'POST' and str(record.author) == str(request.user.username):
        # Check if the slug has not changed
        if record.slug == request.POST.get('slug'):
            # Update the post title and content
            record.title = request.POST.get('title')
            record.content = request.POST.get('content')
            record.save()
            
            # Return a success response
            return HttpResponse("Updated GO HOME <a href='/'>HOME</a>")
    else:
        # Return an error response if the user is not authorized to edit the post
        return HttpResponse("Unauthorized")

def Delete(request, slug):
    # Retrieve the post with the given slug
    record = Post.objects.get(slug=slug)
    
    # Handle GET request to display the post deletion confirmation form
    if request.method == 'GET':
        return render(request, 'NewPost.html', {
            'post': record,
            'target': 'Delete',
            'method': 'POST',
            'action': '/posts/' + slug + '/delete/'
        })
    
    # Handle POST request to delete

    elif request.method == 'POST' and str(request.user.username) == str(record.author):
        record.delete()
        return HttpResponse("Deleted GO HOME <a href='/'>HOME</a>")
    else: 
        return HttpResponse("Unauthorised")
