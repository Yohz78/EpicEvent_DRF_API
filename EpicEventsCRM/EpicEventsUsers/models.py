from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .managers import MyAccountManager
from django.contrib.auth.models import PermissionsMixin


class CustomUser(AbstractBaseUser, PermissionsMixin):
    objects = MyAccountManager()

    SALES = "sales"
    SUPPORT = "support"
    STAFF = "staff"

    USER_TYPE = ((SALES, "Sales"), (SUPPORT, "Support"), (STAFF, "Staff"))

    email = models.EmailField("email address", unique=True, max_length=100)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=20)
    is_staff = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_superuser = models.BooleanField(
        default=False,
    )
    role = models.CharField(choices=USER_TYPE, max_length=20, null=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone_number"]

    def __str__(self):
        return self.email
