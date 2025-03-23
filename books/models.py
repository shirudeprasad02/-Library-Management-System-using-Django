from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class AdminUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        
        # Ensure username is set (Django requires it)
        extra_fields.setdefault("username", email.split("@")[0])

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

class AdminUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)  # Keep username optional
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = AdminUserManager()  # Use the custom manager

    groups = models.ManyToManyField(
        "auth.Group", related_name="admin_users", blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission", related_name="admin_users_permissions", blank=True
    )

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20, unique=True)
    published_date = models.DateField()

    def __str__(self):
        return self.title
