"""
This module contains Django models for our application.

This module defines various Django models used in our application to represent
database tables. It includes models for users, posts, comments, and other data
structures.

"""
import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Custom manager for the UserProfile model
class AccountManager(BaseUserManager):
    """
    creating a user extending from baseUserMode which is django inbuild
    """

    def create_user(self, email, username, password=None):
        """
        # Check if email is provided
        """
        if not email:
            raise ValueError("Please provide an email.")
        # Check if username is provided
        if not username:
            raise ValueError("Please provide a username.")

        # Create a new user instance with normalized email and username
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        # Set the user's password
        user.set_password(password)
        # Save the user to the database
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        """
        Create a superuser by calling create_user with additional settings
        """
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        # Set the user as staff and superuser
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        # Save the user with updated settings
        user.save(using=self._db)
        return user


# Custom user model based on AbstractBaseUser
class UserProfile(AbstractBaseUser):
    """
    Fields for the user profile
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, max_length=200, verbose_name="email")
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  # Indicates if the account is active
    is_staff = models.BooleanField(default=False)  # Indicates staff status
    is_superuser = models.BooleanField(default=False)  # Indicates superuser status

    USERNAME_FIELD = "email"  # Use email as the unique identifier for login
    REQUIRED_FIELDS = [
        "username"
    ]  # Fields required for user creation (in addition to email)

    objects = AccountManager()  # Custom manager for the UserProfile model

    # Check if the user has a specific permission
    def has_perm(self):
        """
        Only superusers have all permissions
        """
        return self.is_admin

    # Check if the user has permissions to access a specific app/module
    def has_module_perms(self):
        """
        Only superusers have all app-level permissions
        """
        return self.is_superuser

    # Define how the user instance is represented as a string
    def __str__(self):
        return f"{self.username}"


# Model for Tags


class TagManager(models.Manager):
    """
    Custom manager for the Tag model.

    This manager can be used to add custom database queries
    or methods related to the Tag model in the future.

    Example:
    To retrieve all tags that start with a specific prefix, you can use:
    ```
    Tag.objects.get_tags_with_prefix('your_prefix')
    ```
    """

    def get_tags_with_prefix(self, prefix):
        """
        Get all tags that start with a specific prefix.
        """
        return self.filter(name__startswith=prefix)


class Tag(models.Model):
    """
    Model representing tags for photos and videos.

    Tags are used to categorize and organize photos and videos.
    Each tag has a unique name.

    Attributes:
        name (str): The name of the tag.
    """

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True)

    def save(self, *args, **kwargs):
        if not self.description:
            self.description = self.name
        super(Tag, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name}"



# Model for Photos


class PhotoManager(models.Manager):
    """
    Custom manager for the Photo model.

    This manager can be used to add custom database queries
    or methods related to the Photo model in the future.

    Example:
    To retrieve all photos with a specific tag, you can use:
    ```
    Photo.objects.get_photos_with_tag('your_tag')
    ```
    """

    def get_photos_with_tag(self, tag_name):
        """
        Get all photos with a specific tag.
        """
        return self.filter(tags__name=tag_name)


class Photo(models.Model):
    """
    Model representing photos.

    Photos can have a title, description, image, and be associated with tags.

    Attributes:
        title (str): The title of the photo.
        description (str): A description of the photo.
        image (ImageField): The image file for the photo.
        tags (ManyToManyField): Tags associated with the photo.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="photos/", null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name="photos")
    objects = PhotoManager()

    def __str__(self):
        return f"{self.title}"


# Model for Videos


class VideoManager(models.Manager):
    """
    Custom manager for the Video model.

    This manager can be used to add custom database queries
    or methods related to the Video model in the future.

    Example:
    To retrieve all videos with a specific tag, you can use:
    ```
    Video.objects.get_videos_with_tag('your_tag')
    ```
    """

    def get_videos_with_tag(self, tag_name):
        """
        Get all videos with a specific tag.
        """
        return self.filter(tags__name=tag_name)


class Video(models.Model):
    """
    Model representing videos.

    Videos can have a title, description, video file, and be associated with tags.

    Attributes:
        title (str): The title of the video.
        description (str): A description of the video.
        video_file (FileField): The video file for the video.
        tags (ManyToManyField): Tags associated with the video.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    video_file = models.FileField(upload_to="videos/", null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name="videos")
    objects = VideoManager()

    def __str__(self):
        return f"{self.title}"
