from django.test import TestCase
from .models import UserProfile, Tag, Photo, Video

class UserProfileModelTestCase(TestCase):

    def test_create_user(self):
        user = UserProfile.objects.create_user(
            email="test@example.com",
            username="testuser",
            password="testpassword"
        )
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.username, "testuser")
        self.assertTrue(user.check_password("testpassword"))

    def test_create_superuser(self):
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

    def test_tag_str_representation(self):
        tag = Tag.objects.create(name="Test Tag")
        self.assertEqual(str(tag), "Test Tag")

class PhotoModelTestCase(TestCase):

    def test_photo_str_representation(self):
        photo = Photo.objects.create(title="Test Photo")
        self.assertEqual(str(photo), "Test Photo")

class VideoModelTestCase(TestCase):

    def test_video_str_representation(self):
        video = Video.objects.create(title="Test Video")
        self.assertEqual(str(video), "Test Video")
