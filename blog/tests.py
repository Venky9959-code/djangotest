from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Post


class PostModelTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title="Test Blog Post",
            content="This is a test content for the blog post."
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Blog Post")
        self.assertEqual(self.post.content, "This is a test content for the blog post.")
        self.assertEqual(str(self.post), "Test Blog Post")


class PostAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.post1 = Post.objects.create(
            title="First Post",
            content="Content for first post"
        )
        self.post2 = Post.objects.create(
            title="Second Post",
            content="Content for second post"
        )

    def test_get_all_posts(self):
        url = reverse('post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_post(self):
        url = reverse('post-detail', kwargs={'pk': self.post1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "First Post")

