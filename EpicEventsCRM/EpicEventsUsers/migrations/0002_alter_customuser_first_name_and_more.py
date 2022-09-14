# Generated by Django 4.1.1 on 2022-09-14 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("EpicEventsUsers", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="first_name",
            field=models.CharField(max_length=25, verbose_name="First Name"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Is an active user"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="is_staff",
            field=models.BooleanField(default=False, verbose_name="Is staff member"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="is_superuser",
            field=models.BooleanField(default=False, verbose_name="Is a superuser"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="last_name",
            field=models.CharField(max_length=25, verbose_name="Last name"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="phone_number",
            field=models.CharField(max_length=20, verbose_name="Phone number"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="role",
            field=models.CharField(
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
    ]