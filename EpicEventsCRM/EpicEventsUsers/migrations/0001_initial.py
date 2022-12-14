# Generated by Django 4.1.1 on 2022-09-15 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=100, unique=True, verbose_name="email address"
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=25, verbose_name="First Name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=25, verbose_name="Last name"),
                ),
                (
                    "phone_number",
                    models.CharField(max_length=20, verbose_name="Phone number"),
                ),
                (
                    "is_staff",
                    models.BooleanField(default=False, verbose_name="Is staff member"),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Is an active user"),
                ),
                (
                    "is_superuser",
                    models.BooleanField(default=False, verbose_name="Is a superuser"),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("sales", "Sales"),
                            ("support", "Support"),
                            ("staff", "Staff"),
                        ],
                        max_length=20,
                        null=True,
                        verbose_name="Role",
                    ),
                ),
                ("date_created", models.DateField(auto_now_add=True)),
                ("date_updated", models.DateField(auto_now_add=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
