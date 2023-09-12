"""
Module Docstring:

This module contains test cases for API views related to user
registration, login, user profile management, and authentication.
"""


from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from django.test import TestCase
from uuid import uuid4  # Import UUID generator


from core.models import  Tag, Photo, Video

User = get_user_model()


class AuthenticationTests(TestCase):
    """
    Test case class for authentication-related API views.
    """

    def setUp(self):
        """
        Set up test data and client for API testing.
        """
        self.user = User.objects.create_user(
            email="test@example.com",
            username="testuser",
            password="testpassword",
        )
        self.admin_user = User.objects.create_superuser(
            email="admin@example.com",
            username="adminuser",
            password="adminpassword",
        )
        self.client = APIClient()

    def test_user_registration(self):
        """
        Test user registration API view.
        """
        url = reverse("register")
        data = {
            "email": "newuser@example.com",
            "username": "newuser",
            "password": "newpassword",
            "first_name": "firstname",
            "last_name": "lastname"
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self):
        """
        Test user login API view.
        """
        url = reverse("login")
        data = {
            "email": "newuser@example.com",
            "password": "newpassword",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
        self.assertIn("admin", response.data)

    # Add more test cases for other authentication-related views...


class TagTests(TestCase):
    """
    Test case class for Tag model and API views.
    """

    def setUp(self):
        """
        Set up test data and client for API testing.
        """
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="test@example.com",
            username="testuser",
            password="testpassword",
        )
        self.tag = Tag.objects.create(name="Test Tag")

    def test_tag_list(self):
        """
        Test Tag list API view.
        """
        url = reverse("tag-list-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_tag_detail(self):
        """
        Test Tag detail API view.
        """
        url = reverse("tag-detail", args=[self.tag.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Add more test cases for other Tag-related views and functionalities...


class PhotoTests(TestCase):
    """
    Test case class for Photo model and API views.
    """

    def setUp(self):
        """
        Set up test data and client for API testing.
        """
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="test@example.com",
            username="testuser",
            password="testpassword",
        )
        self.photo = Photo.objects.create(
            title="Test Photo",
            id=uuid4()  # Generate a UUID for the primary key
        )

    def test_photo_list(self):
        """
        Test Photo list API view.
        """
        url = reverse("photo-list-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_photo_detail(self):
        """
        Test Photo detail API view.
        """
        url = reverse("photo-detail", args=[str(self.photo.id)])  # Convert UUID to string
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Add more test cases for other Photo-related views and functionalities...


class VideoTests(TestCase):
    """
    Test case class for Video model and API views.
    """

    def setUp(self):
        """
        Set up test data and client for API testing.
        """
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="test@example.com",
            username="testuser",
            password="testpassword",
        )
        self.video = Video.objects.create(title="Test Video")

    def test_video_list(self):
        """
        Test Video list API view.
        """
        url = reverse("video-list-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_video_detail(self):
        """
        Test Video detail API view.
        """
        url = reverse("video-detail", args=[str(self.video.id)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Add more test cases for other Video-related views and functionalities...
