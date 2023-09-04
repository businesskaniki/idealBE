"""
API views for user registration, login, user profile management, and authentication.

This module contains Django views and URL configurations for handling user registration,
authentication, user profile management, and CRUD operations for Tag, Photo, and Video objects.
"""

from django.urls import path
from .views import (
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

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("user-profiles/", UserProfileListView.as_view(), name="user-profiles"),
    path("user-profiles/<int:pk>/", UserProfileDetail.as_view(), name="user-profile-detail"),
    path("tags/", TagListCreateView.as_view(), name="tag-list-create"),
    path("tags/<int:pk>/", TagDetailUpdateDeleteView.as_view(), name="tag-detail"),
    path("photos/", PhotoListCreateView.as_view(), name="photo-list-create"),
    path("photos/<int:pk>/", PhotoDetailUpdateDeleteView.as_view(), name="photo-detail"),
    path("videos/", VideoListCreateView.as_view(), name="video-list-create"),
    path("videos/<int:pk>/", VideoDetailUpdateDeleteView.as_view(), name="video-detail"),
]
