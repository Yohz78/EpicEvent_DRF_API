from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator


class Client(models.Model):
    """Client model"""

    first_name = models.CharField("First name", max_length=25)
    last_name = models.CharField("Last name", max_length=25)
    email = models.EmailField("email address", unique=True, max_length=100)
    phone = models.CharField("Phone number", max_length=20)
    mobile = models.CharField("Mobile number", max_length=20)
    company_name = models.CharField("Company", max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    sales_contact = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.email


class Contract(models.Model):
    """Contract model"""

    sales_contact = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField("Has contract been signed ?", default=False)
    amount = models.FloatField("Contract amount", max_length=11)
    payment_due = models.DateTimeField("Payment due date", auto_now_add=False)

    def __str__(self):
        return self.email


class Event(models.Model):
    """Event model"""

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    support_contact = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    status = models.BooleanField("Event status", default=True)
    attendees = models.PositiveIntegerField(
        "Event Attendees", validators=[MinValueValidator(0)]
    )
    event_date = models.DateTimeField("Event date", auto_now_add=False)
    notes = models.TextField("Additional notes", max_length=1000)
