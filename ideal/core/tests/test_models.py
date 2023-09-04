"""
Module docstring: This module contains test cases for the models in your Django application.
"""

from django.test import TestCase
from core.models import UserProfile, Tag, Photo, Video

class UserProfileModelTestCase(TestCase):
    """
    Test cases for the UserProfile model.
    """

    def test_create_user(self):
        """
        Test creating a regular user.
        """
        user = UserProfile.objects.create_user(
            email="test@example.com",
            username="testuser",
            password="testpassword"
        )
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.username, "testuser")
        self.assertTrue(user.check_password("testpassword"))

    def test_create_superuser(self):
        """
        Test creating a superuser.
        """
        superuser = UserProfile.objects.create_superuser(
            email="admin@example.com",
            username="adminuser",
            password="adminpassword"
        )
        self.assertEqual(superuser.email, "admin@example.com")
        self.assertEqual(superuser.username, "adminuser")
        self.assertTrue(superuser.check_password("adminpassword"))
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

class TagModelTestCase(TestCase):
    """
    Test cases for the Tag model.
    """

    def test_tag_str_representation(self):
        """
        Test the string representation of a Tag instance.
        """
        tag = Tag.objects.create(name="Test Tag")
        self.assertEqual(str(tag), "Test Tag")

class PhotoModelTestCase(TestCase):
    """
    Test cases for the Photo model.
    """

    def test_photo_str_representation(self):
        """
        Test the string representation of a Photo instance.
        """
        photo = Photo.objects.create(title="Test Photo")
        self.assertEqual(str(photo), "Test Photo")

class VideoModelTestCase(TestCase):
    """
    Test cases for the Video model.
    """

    def test_video_str_representation(self):
        """
        Test the string representation of a Video instance.
        """
        video = Video.objects.create(title="Test Video")
        self.assertEqual(str(video), "Test Video")
