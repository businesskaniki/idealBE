"""
API views for user registration, login, user profile management, and authentication.

This module contains Django views and URL configurations for handling user registration,
authentication, user profile management, and CRUD operations for Tag, Photo, and Video objects.
"""

from django.urls import path,re_path
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
    re_path(r'^user-profile/(?P<pk>[0-9a-f-]+)/$', UserProfileDetail.as_view(), name="user-profile-detail"),
    path("tags/", TagListCreateView.as_view(), name="tag-list-create"),
    re_path(r'^tags/(?P<pk>[0-9a-f-]+)/$', TagDetailUpdateDeleteView.as_view(), name="tag-detail"),
    path("photos/", PhotoListCreateView.as_view(), name="photo-list-create"),
    re_path(r'^photos/(?P<pk>[0-9a-f-]+)/$', PhotoDetailUpdateDeleteView.as_view(), name="photo-detail"),
    path("videos/", VideoListCreateView.as_view(), name="video-list-create"),
    re_path(r'^videos/(?P<pk>[0-9a-f-]+)/$', VideoDetailUpdateDeleteView.as_view(), name="video-detail"),  # Use re_path with a regex pattern
]
