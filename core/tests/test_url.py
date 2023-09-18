"""
URL tests for API views related to user registration, 
login, user profile management, and CRUD operations for Tag, Photo, and Video objects.
This module defines the URL patterns for the 
API views associated with user registration, authentication,
user profile management, and CRUD operations for Tag, Photo, and Video objects.
"""


from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core.views import (
    RegisterView,
    LoginView,
    UserProfileListView,
    UserProfileDetail,
    TagListCreateView,
    TagDetailUpdateDeleteView,
    PhotoListCreateView,
    PhotoDetailUpdateDeleteView,
    VideoListCreateView,
    VideoDetailUpdateDeleteView,
)

class TestUrls(SimpleTestCase):
    """
    Test case class for URL routing.
    """
    def test_register_url_resolves(self):
        """
        Test if the 'register' URL resolves to the RegisterView class.
        """
        url = reverse("register")
        self.assertEqual(resolve(url).func.view_class, RegisterView)

    def test_login_url_resolves(self):
        """
        Test if the 'login' URL resolves to the LoginView class.
        """
        url = reverse("login")
        self.assertEqual(resolve(url).func.view_class, LoginView)

    def test_user_profiles_url_resolves(self):
        """
        Test if the 'user-profiles' URL resolves to the UserProfileListView class.
        """
        url = reverse("user-profiles")
        self.assertEqual(resolve(url).func.view_class, UserProfileListView)

    def test_user_profile_detail_url_resolves(self):
        """
        Test if the 'user-profile-detail' URL resolves to the UserProfileDetail class.
        """
        url = reverse("user-profile-detail", args=[1])
        self.assertEqual(resolve(url).func.view_class, UserProfileDetail)

    def test_tags_url_resolves(self):
        """
        Test if the 'tags' URL resolves to the TagListCreateView class.
        """
        url = reverse("tag-list-create")
        self.assertEqual(resolve(url).func.view_class, TagListCreateView)

    def test_tag_detail_url_resolves(self):
        """
        Test if the 'tag-detail' URL resolves to the TagDetailUpdateDeleteView class.
        """
        url = reverse("tag-detail", args=[1])
        self.assertEqual(resolve(url).func.view_class, TagDetailUpdateDeleteView)

    def test_photos_url_resolves(self):
        """
        Test if the 'photos' URL resolves to the PhotoListCreateView class.
        """
        url = reverse("photo-list-create")
        self.assertEqual(resolve(url).func.view_class, PhotoListCreateView)

    def test_photo_detail_url_resolves(self):
        """
        Test if the 'photo-detail' URL resolves to the PhotoDetailUpdateDeleteView class.
        """
        url = reverse("photo-detail", args=[1])
        self.assertEqual(resolve(url).func.view_class, PhotoDetailUpdateDeleteView)

    def test_videos_url_resolves(self):
        """
        Test if the 'videos' URL resolves to the VideoListCreateView class.
        """
        url = reverse("video-list-create")
        self.assertEqual(resolve(url).func.view_class, VideoListCreateView)

    def test_video_detail_url_resolves(self):
        """
        Test if the 'video-detail' URL resolves to the VideoDetailUpdateDeleteView class.
        """
        url = reverse("video-detail", args=[1])
        self.assertEqual(resolve(url).func.view_class, VideoDetailUpdateDeleteView)
