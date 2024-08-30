from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post
from django.utils.text import slugify

class PostModelTest(TestCase):

    def setUp(self):
        """
        Set up the initial test data for the test case.
        Creates a user and a post instance associated with that user.
        """
        # Create a user to associate with the post
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Create a post instance with a title, content, and the created user as the author
        self.post = Post.objects.create(
            title='Test Post Title',
            content='This is the content of the post.',
            author=self.user
        )

    def test_post_creation(self):
        """
        Test that the Post object is created with the correct attributes.
        """
        # Retrieve the post from the database using its ID
        post = Post.objects.get(id=self.post.id)
        
        # Assert that the post's title matches the expected title
        self.assertEqual(post.title, 'Test Post Title')
        
        # Assert that the post's content matches the expected content
        self.assertEqual(post.content, 'This is the content of the post.')
        
        # Assert that the post's author matches the created user
        self.assertEqual(post.author, self.user)

    def test_slug_generation(self):
        """
        Test that the slug is generated correctly from the post title.
        """
        # Retrieve the post from the database using its ID
        post = Post.objects.get(id=self.post.id)
        
        # Generate the expected slug from the post title using slugify
        expected_slug = slugify('Test Post Title')
        
        # Assert that the post's slug matches the expected slug
        self.assertEqual(post.slug, expected_slug)

    def test_timestamps(self):
        """
        Test that the creation and update timestamps are set correctly.
        """
        # Assert that the created_at and updated_at fields are not None
        self.assertIsNotNone(self.post.created_at)
        self.assertIsNotNone(self.post.updated_at)

        # Update the post's content and save the changes to trigger an update
        self.post.content = 'Updated content.'
        self.post.save()

        # Retrieve the updated post from the database
        updated_post = Post.objects.get(id=self.post.id)
        
        # Assert that the updated_at timestamp is greater than or equal to the created_at timestamp
        self.assertGreaterEqual(updated_post.updated_at, self.post.created_at)

    def test_post_str(self):
        """
        Test the string representation of the Post model.
        """
        # Assert that the string representation of the post matches the post title
        self.assertEqual(str(self.post), 'Test Post Title')
