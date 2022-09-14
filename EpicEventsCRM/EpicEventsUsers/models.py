from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import MyAccountManager
from django.contrib.auth.models import PermissionsMixin


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Custom user model"""

    objects = MyAccountManager()

    SALES = "sales"
    SUPPORT = "support"
    STAFF = "staff"

    USER_TYPE = ((SALES, "Sales"), (SUPPORT, "Support"), (STAFF, "Staff"))

    email = models.EmailField("email address", unique=True, max_length=100)
    first_name = models.CharField("First Name", max_length=25)
    last_name = models.CharField("Last name", max_length=25)
    phone_number = models.CharField("Phone number", max_length=20)
    is_staff = models.BooleanField(
        "Is staff member",
        default=False,
    )
    is_active = models.BooleanField(
        "Is an active user",
        default=True,
    )
    is_superuser = models.BooleanField(
        "Is a superuser",
        default=False,
    )
    role = models.CharField("Role", choices=USER_TYPE, max_length=20, null=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone_number"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
