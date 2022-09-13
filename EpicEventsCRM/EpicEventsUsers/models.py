from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.postgres.fields import CIEmailField


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password):
        if not email:
            raise ValueError("Please enter a valid email address.")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    objects = MyAccountManager()

    SALES = "sales"
    SUPPORT = "support"
    STAFF = "staff"

    USER_TYPE = ((SALES, "Sales"), (SUPPORT, "Support"), (STAFF, "Staff"))

    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=20)
    is_staff = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=True,
    )
    role = models.CharField(choices=USER_TYPE, max_length=20, null=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone_number"]
