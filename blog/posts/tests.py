from django.test import TestCase, Client
from django.contrib.auth.models import User
from api.models import Post

class PostDeleteTestCase(TestCase):
    def setUp(self):
        """
        Set up the test environment:
        - Create two users: one who is an author and one who is not.
        - Create a post associated with the author.
        - Initialize a Django test client for simulating HTTP requests.
        """
        # Create test users
        self.author = User.objects.create_user(username='author', password='password')
        self.non_author = User.objects.create_user(username='non_author', password='password')
        
        # Create a test post
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            content='This is a test post.',
            author=self.author
        )
        
        # Create a client instance for simulating requests
        self.client = Client()
        
    def test_delete_post_as_author(self):
        """
        Test case to verify that the post author can successfully delete their own post.
        """
        # Log in as the author
        self.client.login(username='author', password='password')
        
        # Send a POST request to delete the post
        response = self.client.post(f'/posts/{self.post.slug}/delete/')
        
        # Check if the response indicates success and the post is removed from the database
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Deleted GO HOME")
        self.assertFalse(Post.objects.filter(slug=self.post.slug).exists())
        
    def test_delete_post_as_non_author(self):
        """
        Test case to verify that a user who is not the author cannot delete the post.
        """
        # Log in as a non-author
        self.client.login(username='non_author', password='password')
        
        # Send a POST request to delete the post
        response = self.client.post(f'/posts/{self.post.slug}/delete/')
        
        # Check if the response indicates unauthorized access and the post is still present in the database
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Unauthorised")
        self.assertTrue(Post.objects.filter(slug=self.post.slug).exists())
        
    def test_delete_post_while_not_logged_in(self):
        """
        Test case to verify that a user who is not logged in cannot delete the post.
        """
        # Send a POST request to delete the post without logging in
        response = self.client.post(f'/posts/{self.post.slug}/delete/')
        
        # Check if the response indicates unauthorized access and the post is still present in the database
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Unauthorised")
        self.assertTrue(Post.objects.filter(slug=self.post.slug).exists())
