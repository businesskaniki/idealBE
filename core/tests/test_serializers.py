from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from core.models import UserProfile, Tag, Photo, Video
from core.serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserProfileSerializer,
    TagSerializer,
    VideoSerializer,
    PhotoSerializer
)

User = get_user_model()


class RegisterSerializerTest(TestCase):
    """
    Test case for the `RegisterSerializer` serializer.
    """

    def test_serializer(self):
        """
        Test valid registration data.
        """
        data = {
            "email": "newuser@example.com",
            "username": "newuser",
            "first_name": "John",
            "last_name": "Doe",
            "password": "newpassword",
        }

        serializer = RegisterSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_invalid_data(self):
        """
        Test registration with incomplete data (invalid data).
        """
        data = {
            "email": "newuser@example.com",
            "username": "newuser",
        }

        serializer = RegisterSerializer(data=data)
        self.assertFalse(serializer.is_valid())


class LoginSerializerTest(TestCase):
    """
    Test case for the `LoginSerializer` serializer.
    """

    def test_serializer(self):
        """
        Test valid login data.
        """
        user = UserProfile.objects.create_user(
            email="test@example.com",
            username="testuser",
            password="testpassword",
        )

        data = {
            "email": "test@example.com",
            "password": "testpassword",
        }

        serializer = LoginSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_invalid_data(self):
        """
        Test login with incomplete data (invalid data).
        """
        data = {
            "email": "test@example.com",
        }

        serializer = LoginSerializer(data=data)
        self.assertFalse(serializer.is_valid())


class UserProfileSerializerTest(TestCase):
    """
    Test case for the `UserProfileSerializer` serializer.
    """

    def test_serializer(self):
        """
        Test updating user profile data.
        """
        user = UserProfile.objects.create_user(
            email="test@example.com",
            username="testuser",
            password="testpassword",
        )

        data = {
            "email": "updated@example.com",
            "username": "updateduser",
            "first_name": "Updated",
            "last_name": "User",
        }

        serializer = UserProfileSerializer(user, data=data)
        self.assertTrue(serializer.is_valid())
        updated_user = serializer.save()
        self.assertEqual(updated_user.email, data["email"])
        self.assertEqual(updated_user.username, data["username"])
        self.assertEqual(updated_user.first_name, data["first_name"])
        self.assertEqual(updated_user.last_name, data["last_name"])


class TagSerializerTest(TestCase):
    """
    Test case for the `TagSerializer` serializer.
    """

    def test_serializer(self):
        """
        Test that the serializer includes the 'name' field.
        """
        tag = Tag.objects.create(name="Test Tag")
        serializer = TagSerializer(tag)
        self.assertIn("name", serializer.data)


class PhotoSerializerTest(TestCase):
    """
    Test case for the `PhotoSerializer` serializer.
    """

    def test_serializer(self):
        """
        Test that the serializer includes the 'title' field.
        """
        photo = Photo.objects.create(title="Test Photo")
        serializer = PhotoSerializer(photo)
        self.assertIn("title", serializer.data)


class VideoSerializerTest(TestCase):
    """
    Test case for the `VideoSerializer` serializer.
    """

    def test_serializer(self):
        """
        Test that the serializer includes the 'title' field.
        """
        video = Video.objects.create(title="Test Video")
        serializer = VideoSerializer(video)
        self.assertIn("title", serializer.data)
