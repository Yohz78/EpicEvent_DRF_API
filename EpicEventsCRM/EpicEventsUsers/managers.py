from django.db import models
from django.contrib.auth.models import BaseUserManager


class MyAccountManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier for authentication
    """

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Please enter a valid email address.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(
            email=self.normalize_email(email), password=password, **extra_fields
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
